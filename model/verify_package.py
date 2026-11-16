"""Compatibility entry point for the reorganized repository verifier."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
result = subprocess.run([sys.executable, str(root / 'tools/verify_repository.py')])
sys.exit(result.returncode)
