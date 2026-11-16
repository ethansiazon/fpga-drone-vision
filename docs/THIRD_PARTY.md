# Third-party material

Ultralytics YOLOv5 v7.0 is included under model/software/vendor/yolov5 with its GPL-3.0 license and source notices. The adapted detector depends on that source. Preserve applicable license obligations when distributing or changing the model software.

Camera register recipes credit Espressif esp32-camera. The supplied Apache 2.0 license is in licenses/ESPRESSIF_APACHE_2_0.txt. Source URLs and hashes remain in hardware/camera/r13/scripts/camera_trials.json. The previously inspected ov5640.c also carried an OpenMV MIT notice; that full driver was not copied into this package.

AMD/Xilinx generated HDL retains its vendor notices and tool-version metadata. Use the appropriate licensed vendor tools and IP. No new blanket license is asserted over vendor assets, teammate code, or the mixed repository.

Micron/MIG behavioral simulation models without an included redistribution license are external dependencies. The board source retains the expected filenames and regeneration context.

Weights, quantization metadata, and compact numerical test vectors retain their original hashes and provenance. Training/validation manifests identify the source data. Bulk images, videos, and private captures remain external and subject to their providers' terms.

Original handoff notices are preserved in docs/history/THIRD_PARTY.md. Those notes refer to the former private workspace. This destination repository is public, and the selected publication scope is recorded in docs/MIGRATION.md.
