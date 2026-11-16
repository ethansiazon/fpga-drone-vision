# Software quick start

Use Python 3.12. The commands below run from the repository root in PowerShell.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install torch==2.4.1 torchvision==0.19.1 --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r model/software/requirements.txt
python tools/verify_repository.py
.\.venv\Scripts\python.exe model/software/inspect_model.py --report local_results/model_check/model.json
```

The inspection verifies both retained checkpoint hashes, loads the EMA architecture strictly, checks the 331,114 parameter count and head shapes, and compares floating/fixed outputs on a seeded random input. It does not measure accuracy.

Run your own unannotated source video with a new output filename.

```powershell
.\.venv\Scripts\python.exe model/software/run_video.py --input C:/videos/source.mp4 --output local_results/replay.mp4
```

For a short functional run, add `--max-frames 20`. The runner creates the annotated video, per-frame JSONL records, and a summary. It preserves existing outputs and stops below the RAM reserve. Only load the trusted checkpoint files whose hashes are recorded in this repository.

This CPU reference keeps the R9 motion/crop/association logic and fixed-point arithmetic. Its 10 updates/s and 90 ms availability are simulated source-time settings. Wall-clock replay speed does not establish FPGA speed.

Dataset images and demo videos remain external. Use your own file or obtain the source data under the provider's terms. Historical gallery and smoke filenames in imported notes refer to the original local handoff.
