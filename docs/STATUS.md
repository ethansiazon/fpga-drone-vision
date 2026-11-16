# Current status

Reviewed 16 November 2026 from the saved local project and supplied build notes.

## Retained detector

V5 epoch 8 uses 331,114 learned parameters, a 256 × 192 RGB region, a narrow YOLOv5 v7.0-derived backbone with C3/ReLU blocks, and P2/P3 detection heads. Three anchors per cell each hold box coordinates, objectness, and two class scores. The decoder derives the centre from the predicted box. Frozen weights and fixed-point metadata are in model/.

The R9 software pipeline adds motion proposals, approximate camera translation compensation, crop/letterbox preprocessing, and one-target association. It was the retained configuration for the preferred demonstrations. Its recorded validation produced 6,917 correct boxes from 8,651 drone frames, with 82.83% precision and 81.37% F1. Related development footage and source-specific weaknesses limit those results.

## Camera baseline

R13 is the physically preferred camera-only version after automatic white balance settles. It captures RGB565 at 320 × 240, with approximately 20 camera FPS and a majority filter for short signal glitches. HDMI is 640 × 480 at 60 Hz using 25.2 MHz pixel and 126 MHz serializer clocks. Display refresh differs from camera FPS.

Upward-moving shadow bands remained in some indoor scenes. The cause was not established. The separate 30 FPS experiments developed frame-alignment problems and were not promoted. The frozen R13 source and original bitstream are included here. Manual picture settings saved in another lighting condition do not establish universal calibration.

## Saved live-camera integration

The supplied Genesys 2 rev-3 bitstream was built with Vivado 2023.2 on 6 November. Teammate notes describe 320 × 240 camera capture, three DDR3 image buffers, a fixed 256 × 192 centre crop, CNN at 140 MHz, decoding, HDMI overlays, and POSITION transmission through JD1.

Those notes report about 53 ms CNN-plus-decoder processing, 10 reports/s, and 78.08 ms capture-to-POSITION latency over 241 frames. Reported resources are 69,001 LUTs, 376 BRAM, and 310 DSPs, with +0.018 ns setup slack. These are supplied results, not new measurements taken while publishing this repository. The BRAM entry lacks a detailed current report here, so preserve its reported unit when quoting it.

The exact rev-3 integration source, corresponding constraints, build configuration, and raw latency logs are missing from the available handoff. The included hardware/genesys2/reference_oct29 source is an older standalone implementation. Its reports must remain associated with that older build.

## Remaining work

- Obtain the exact source commit and detailed reports for the integrated bitstream.
- Record frame identifiers and age through buffering, inference, decoding, and the outgoing position message.
- Check latest-frame selection and buffer ownership under continuous capture.
- Verify the protocol, coordinate convention, and behavior on missing detections.
- Evaluate real daylight camera footage, including background clutter, motion, and empty scenes.
- Keep software replay accuracy separate from live-camera hardware accuracy and end-to-end response.

No board was programmed and no model was retrained during this repository migration.
