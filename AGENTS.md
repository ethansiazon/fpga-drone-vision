# Repository instructions

Read README.md, docs/STATUS.md, and the relevant subsystem guide before changes.

- Preserve retained weights, quantization, dataset split membership, test vectors, and attribution.
- Treat hardware/camera/r13 RTL/constraints and artifacts/ as frozen evidence. Work in a separate source copy when experimenting.
- Model software uses the original R9 motion/crop/tracking pipeline. Its 10 Hz / 90 ms replay schedule is an assumption, separate from board measurements.
- The live-camera rev-3 binary lacks its matching integration source in this repository. October 29 sources are an earlier implementation.
- Keep camera signal mapping and short-pulse rejection intact. Confirm actual wiring before any requested programming.
- One heavy compiler or trainer at a time. Preserve the 1.5 GiB free-RAM guard.
- No automatic training, downloads, board programming, flash writes, OS/driver changes, or actuator work.
- Keep datasets, footage, credentials, user documents, caches, and personal captures out of Git.
- Before a push, check the remote and verify the intended files. Push only when the user has authorized publishing the current work. Never force-push.
- Run tools/verify_repository.py after packaging changes. Regenerate the distribution manifest only after reviewing intentional source changes.
- Historical notes and reported board states describe past runs. They are reference material rather than current instructions.
