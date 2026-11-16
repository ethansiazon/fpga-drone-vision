# FPGA Drone Vision

Drone detection for the Digilent Genesys 2, using an OV5640 camera and a compact YOLOv5-derived CNN. This repository contains the retained trained model, software replay, fixed-point reference, FPGA source, camera tools, test evidence, and saved camera/CNN bitstreams.

The retained model is **V5 epoch 8**, with **331,114 parameters** and a **256 × 192 RGB input**. Its preferred software configuration is **R9**. The proven camera baseline is **R13**, using 320 × 240 RGB565 capture at approximately 20 FPS.

## Start here

| Task | Location |
|---|---|
| Understand the current result and its limits | [Current status](docs/STATUS.md) |
| Run the retained detector on a local video | [Software setup](docs/QUICKSTART.md) |
| Inspect weights, architecture, preprocessing, and training records | [Model](model/README.md) |
| Continue the camera work or adjust image settings | [Camera guide](hardware/camera/README.md) |
| Find the shipped live-camera CNN bitstream | [Artifacts](artifacts/README.md) |
| Study the rebuildable older DDR/CNN integration | [Genesys 2 source](hardware/genesys2/README.md) |
| Review numerical, software, and hardware evidence | [Evidence guide](docs/EVIDENCE.md) |
| Check file integrity after cloning | `python tools/verify_repository.py` |

## Layout

```text
model/                 Trained weights, architecture, CPU replay, HLS/RTL, evidence
hardware/camera/       Frozen R13 source, wiring, simulation, UART image tools
hardware/genesys2/     October 29 DDR/CNN reference implementation
artifacts/            Selected camera and live-camera CNN bitstreams with hashes
tools/                Integrity checks and camera test/build entry points
docs/                 Setup, current status, evidence, research, provenance
licenses/             Preserved third-party license material
archive/              Original beginner exercises from this repository
```

## Results

| Scope | Saved result |
|---|---|
| V5/R9 software replay | Correct-box recall 79.96%, precision 82.83%, F1 81.37% |
| Empty-frame software outputs | 3 of 328 true empty frames |
| October 29 board test | 96 of 100 selected positive images had centres within 32 pixels |
| November live-camera build | Teammate reports about 10 position updates/s and 78.08 ms capture-to-POSITION latency |

Software metrics include the R9 motion proposals and tracking policy. The shipped live-camera build uses a fixed centre crop. The software metrics do not establish that build's field accuracy. The selected positive-image test does not measure precision or false detections. Read the [evidence guide](docs/EVIDENCE.md) before quoting a result.

## Source and build coverage

The saved live-camera rev-3 bitstream combines R13 capture, DDR3 buffers, CNN inference, decoding, HDMI overlays, and a position output. Its exact November integration source and detailed measurement logs were supplied through a separate teammate repository and are absent from the available local handoff. Its metadata is preserved with the binary.

The camera source and older October 29 board implementation are included. Rebuilding that older implementation produces an earlier standalone image-input system. Obtaining the matching rev-3 source remains necessary for a reproducible rebuild of the shipped integrated binary.

Original experiments, datasets, footage, build caches, and other group subsystems remain in their existing local locations. Dataset manifests and compact numerical test vectors accompany the model. See [migration details](docs/MIGRATION.md) for the selected files and provenance.

## Credits and licenses

Ethan Siazon developed the retained camera/software work with the project team. Niko Warren supplied the October 29 Genesys 2 integration and the later live-camera build. The model adapts Ultralytics YOLOv5 v7.0. Research and implementation references appear in [research](docs/RESEARCH.md) and [third-party notices](docs/THIRD_PARTY.md). Component licenses and vendor notices apply to their respective files.
