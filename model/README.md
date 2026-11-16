# Retained V5 epoch-8 detector

## Contents

| Folder | Purpose |
|---|---|
| weights/ | Floating EMA checkpoint and trusted fixed-point model |
| software/ | Architecture, CPU inference, preprocessing, integer decoder, R9 tracking, YOLOv5 vendor source |
| config/ | Preferred R9 settings, trained anchors, head shapes, and decoder metadata |
| fpga/ | CNN/decoder HLS, generated RTL, coefficients, numerical vectors, and core reports |
| evidence/ | Saved training/configuration/split records and validation outputs |
| checks/historical/ | Original model-load and replay-parity evidence |
| reference_source/ | Original training/export/evaluation dependency closure |

## Architecture and numbers

The CNN accepts a 256 × 192 RGB crop and has 331,114 learned parameters. It adapts YOLOv5 v7.0 with a narrow backbone, C3 blocks, and ReLU. Its P2 head is 64 × 48 × 21 and its P3 head is 32 × 24 × 21. Each cell has three anchors with seven fields each. The decoder handles box coordinates, objectness, and mapping back into image coordinates. Class fields are not validated aircraft rejection in the shipped selection policy.

The hardware reference uses 16-bit per-layer-scaled weights and 24-bit activations/bias values with 14 fractional bits. Accumulators are wider. Output storage uses 32-bit lanes for the integer decoder. Exact scales, rounding, saturation, tensor order, and offsets appear in fpga/cnn_hls/QUANTIZED_MODEL_METADATA.json and the implementation.

The software pipeline adds motion proposals, crop/letterbox processing, and R9 single-target association. Preserve those operations when comparing against the saved application metrics. The hardware rev-3 fixed crop has a different surrounding pipeline.

## Using and continuing the model

Start with [the quick start](../docs/QUICKSTART.md). Run software/inspect_model.py before inference. FPGA entry points and limits appear in [the FPGA guide](fpga/README.md).

The epoch_08.pt file contains an internal next-epoch recovery counter of 9. It represents eight completed additional epochs from the earlier checkpoint. The original datasets and earlier initialization checkpoint are external. The reference_source scripts retain historical machine paths and need adaptation for retraining. The manifests preserve original split membership and provenance.

The checkpoint SHA256 values are fixed in config/PREFERRED_INFERENCE_R9.json and checked before loading. The import manifest and repository distribution manifest provide additional file integrity checks. The original handoff-wide manifest lives under docs/provenance and includes historical local files outside this distribution.

Read [evidence](../docs/EVIDENCE.md), [research](../docs/RESEARCH.md), and [third-party notices](../docs/THIRD_PARTY.md) before reusing claims or code.
