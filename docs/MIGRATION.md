# Repository migration

Prepared 16 November 2026 from the retained local genesys2-camera-cnn project. The import commit, source paths, byte counts, and original SHA256 hashes are recorded in provenance/IMPORT_MANIFEST.json.

## Selected layout

- cnn/ became model/, retaining the internal layout required by inference, pickled checkpoints, HLS vectors, and historical evidence.
- The frozen R13 source became hardware/camera/r13/. Its RTL and constraints retain their exact bytes. Current host tools and compatible simulation fixtures were copied alongside it.
- fpga_system/ became hardware/genesys2/reference_oct29/ to distinguish its older source from the supplied newer live-camera bitstream.
- The integrated Genesys binary and LTX became artifacts/genesys2/live_camera_rev3/. The camera-only R13 binary and matching reports became artifacts/camera/r13/.
- The destination's original beginner exercises and README remain in archive/beginner_exercises/, with their Git history preserved.

## Entry-point changes

Root tools now point to hardware/camera/r13. The camera build/project defaults select RGB565 and the tested R13 profile. The camera test runner omits newer saved-picture/30 FPS fixtures unsupported by that frozen source. UART session output paths now resolve relative to this repository. These edits affect packaging and build selection, without changing the frozen R13 RTL, retained model weights, or original decoder arithmetic.

The original model handoff checksum index is preserved under provenance/original_model_handoff_sha256.json. It includes historical files outside this distribution. Use provenance/DISTRIBUTION_SHA256.json and tools/verify_repository.py for this repository's actual contents.

## External and historical items

Bulk datasets, footage, personal photos, raw captures, environment directories, Vivado caches/checkpoints, rejected camera trials, and the separate Basys actuator binary remain outside this repository. Data manifests, compact numerical vectors, original licensing, and selected reports are retained.

The Micron behavioral DDR3 simulation models are external because the provided copies lacked an accompanying redistribution license. Obtain them under the provider's terms when running the legacy full-MIG simulation.

The exact source and detailed reports for the shipped integrated rev-3 bitstream are still external to the available handoff. Its checksum and original build description are included. The earlier board source cannot reconstruct that newer binary.

Original local source folders were preserved. No training, FPGA programming, Windows changes, or actuator changes formed part of this migration.
