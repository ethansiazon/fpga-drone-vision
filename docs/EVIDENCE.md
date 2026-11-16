# Results and their scope

## Software application validation

Preferred R9 uses the retained V5 epoch-8 weights, motion proposals, approximate camera-translation compensation, crop/letterbox processing, and one-target association. Its replay schedules up to 10 observation updates/s with assumed 90 ms availability.

Saved correct-box validation reports recall 79.96% (6,917/8,651 drone frames), precision 82.83%, and F1 81.37%. Correct boxes require IoU at least 0.5. Outputs occurred on 3/328 true empty frames. The saved application metric excludes other-aircraft frames, and related frames from the same recordings are correlated. Development footage is not an independent field test.

See model/config/PREFERRED_INFERENCE_R9.json and model/evidence/preferred_r9/. Earlier baseline results use different acquisition settings and remain under model/evidence/baseline_report/.

## Numerical and RTL checks

model/fpga/cnn_hls contains frozen input/coefficient vectors and expected outputs. model/fpga/decoder_hls contains decoder cases and checks. model/checks/historical preserves original load/shape and portable replay-parity results. model/fpga/cnn_rtl_simulation contains the recorded RTL harness/results.

A new package inspection result appears under docs/validation/ after publication checks. This verifies loading and packaging, without establishing new accuracy.

## Isolated core and older board implementation

The isolated CNN routed at 100 MHz with 13.16% LUT, 23.37% BRAM, and 31.67% DSP use. That result omits the rest of the live system. The October 29 DDR/CNN/decoder reference has separate reports under hardware/genesys2/reference_oct29/vivado/.

The October 29 board benchmark used 100 selected positive images from ten recordings. Ninety-six centres fell within 32 pixels in 256 × 192 coordinates. This measures that selected centre-error test rather than precision, recall, or 96% universal accuracy. The CSV evidence has one large outlier in V_DRONE_045 and three in V_DRONE_078, correcting the old handoff's prose.

## Supplied November live-camera build

The original notes report approximately 20 camera FPS, 10 position reports/s, 53 ms CNN-plus-decoder time, and 78.08 ms capture-to-POSITION over 241 frames. They list 69,001 LUT, 376 BRAM, 310 DSP, and +0.018 ns WNS. The raw measurement logs and matching source are external to the available handoff. Preserve those limits when quoting the numbers.

The integration uses a fixed centre crop. The software pipeline's motion search and tracker are different. The earlier software validation figures therefore do not establish the integrated system's field performance.
