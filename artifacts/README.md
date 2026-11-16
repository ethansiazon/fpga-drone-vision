# Selected bitstreams

| Artifact | Scope | Evidence |
|---|---|---|
| camera/r13/camera_hdmi.bit | Preferred camera-only R13 build, RGB565, approximately 20 FPS | Frozen source, routed reports, checksum, and recorded user observations |
| genesys2/live_camera_rev3/cnn_subsystem_top.bit | Supplied live camera, DDR3, centre crop, CNN, decoder, HDMI, position output | Original checksum and teammate build notes |

Each binary targets the Genesys 2 Kintex-7 part. The LTX file beside the integrated binary supplies its JTAG debug-core description. It is not a weight file. Confirm the hardware and intended build before programming. Repository verification never programs a board.

The integrated binary was built with Vivado 2023.2 on 6 November 2026. The camera-only source/build was verified with Vivado 2026.1. Tool versions belong to their respective artifacts.

The integrated binary's exact source is absent from this distribution. Its original supplied notes remain in docs/history/shipped_bitstreams_20261109.md. The Basys section of those historical notes describes a separate group subsystem and a known boot-dependent setting. That Basys binary is outside this camera/CNN repository.

Run `python tools/verify_repository.py` to check the distribution manifest, retained model hashes, original integrated-binary checksums, and frozen R13 source hashes.
