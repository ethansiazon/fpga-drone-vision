"""Verify the packaged files without loading checkpoints or accessing hardware."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'docs/provenance/DISTRIBUTION_SHA256.json'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def sha256(path):
    result = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(chunk)
    return result.hexdigest()


def files_for_distribution():
    output = subprocess.check_output([
        'git', '-C', str(ROOT), 'ls-files', '-z', '--cached', '--others',
        '--exclude-standard',
    ])
    names = sorted(set(output.decode('utf-8').split('\0')) - {''})
    result = []
    for name in names:
        path = ROOT / name
        if path == MANIFEST or not path.is_file():
            continue
        if not path.resolve().is_relative_to(ROOT):
            raise RuntimeError(f'File resolves outside the repository: {name}')
        result.append((name, path))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest', action='store_true',
                        help='Record reviewed intentional changes before verification')
    args = parser.parse_args()
    checks = []
    preferred = read_json(ROOT / 'model/config/PREFERRED_INFERENCE_R9.json')
    for name, key in [('epoch_08.pt', 'checkpoint_sha256'),
                      ('quantized_fx.pt', 'quantized_model_sha256')]:
        path = ROOT / 'model/weights' / name
        if sha256(path) != preferred[key]:
            raise RuntimeError(f'Retained checkpoint mismatch: {name}')
    checks.append('retained checkpoint hashes')

    camera = ROOT / 'hardware/camera/r13'
    for relative, expected in read_json(ROOT / 'artifacts/camera/r13/SOURCE_SHA256.json').items():
        if sha256(camera / relative) != expected:
            raise RuntimeError(f'Frozen camera source mismatch: {relative}')
    camera_status = read_json(ROOT / 'artifacts/camera/r13/STATUS.json')
    if sha256(ROOT / 'artifacts/camera/r13/camera_hdmi.bit') != camera_status['bitstream_sha256']:
        raise RuntimeError('Camera bitstream mismatch')
    checks.append('frozen R13 source and camera bitstream')

    integrated = ROOT / 'artifacts/genesys2/live_camera_rev3'
    for row in (integrated / 'SHA256SUMS').read_text().splitlines():
        if row.strip():
            expected, name = row.split(maxsplit=1)
            path = integrated / name.strip().removeprefix('*')
            if sha256(path) != expected:
                raise RuntimeError(f'Integrated artifact mismatch: {path.name}')
    checks.append('supplied integrated bitstream and debug map')

    imported = read_json(ROOT / 'docs/provenance/IMPORT_MANIFEST.json')
    revised = set(imported['revised_entry_points'])
    for item in imported['files']:
        if item['path'] in revised:
            continue
        if sha256(ROOT / item['path']) != item['source_sha256']:
            raise RuntimeError(f'Imported bytes changed: {item["path"]}')
    checks.append('unmodified imported source and evidence')

    files = files_for_distribution()
    forbidden_parts = {'.git', '.venv', '__pycache__', 'local_results', 'local_artifacts'}
    token_pattern = re.compile(
        rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|'
        rb'\bgh[pousr]_[A-Za-z0-9]{30,}\b|'
        rb'\bgithub_pat_[A-Za-z0-9_]{50,}\b|'
        rb'\bAKIA[A-Z0-9]{16}\b'
    )
    for name, path in files:
        if any(part in forbidden_parts for part in path.relative_to(ROOT).parts):
            raise RuntimeError(f'Local/generated file entered publication: {name}')
        if path.suffix.lower() in {'.mp4', '.mov', '.avi', '.jpg', '.jpeg', '.png'}:
            raise RuntimeError(f'Image/video requires a separate publication review: {name}')
        if path.stat().st_size >= 95 * 1024 * 1024:
            raise RuntimeError(f'File is too large for this Git distribution: {name}')
        if token_pattern.search(path.read_bytes()):
            raise RuntimeError(f'Credential-like content requires review: {name}')
    checks.append('publication file sizes, generated-file exclusions, credential-pattern scan')

    current = {name: sha256(path) for name, path in files}
    if args.write_manifest:
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text(json.dumps(current, indent=2) + '\n', encoding='utf-8')
    if not MANIFEST.exists():
        raise RuntimeError('Missing distribution manifest')
    expected = read_json(MANIFEST)
    if current != expected:
        changed = sorted(name for name in set(current) | set(expected)
                         if current.get(name) != expected.get(name))
        raise RuntimeError('Distribution differs from its manifest: ' + ', '.join(changed[:12]))
    checks.append('complete distribution manifest')
    print(json.dumps({'passed': True, 'files': len(files),
                      'bytes': sum(path.stat().st_size for _, path in files),
                      'checks': checks,
                      'scope': 'Package integrity and publication checks; no hardware access or accuracy measurement.'},
                     indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f'FAILED: {error}', file=sys.stderr)
        sys.exit(1)
