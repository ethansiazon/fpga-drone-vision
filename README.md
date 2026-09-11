# FPGA Drone Vision

Beginner computer-vision exercises for an FPGA lab project. The current code opens one RGB dataset image and displays its provided bounding-box annotation on a separate preview.

## Current progress

- Python starter script runs successfully.
- First dataset frame opens as a 1920 x 1080 RGB image.
- Annotation preview was visually checked: the rectangle surrounds the drone.
- CNN training and FPGA implementation have not started.

## Files

| File | Purpose |
| --- | --- |
| `01_hello.py` | Verify Python runs |
| `02_open_image.py` | Open the first image and print its dimensions and color mode |
| `03_show_annotation.py` | Read the first annotation and draw a box on a copy |

## Setup

These lessons were checked with Python 3.12 and Pillow 10.2.0. Install Pillow in your chosen Python environment:

```sh
python -m pip install -r requirements.txt
```

Download the [DUT Anti-UAV Tracking Dataset](https://www.kaggle.com/datasets/bninaayoub/dut-anti-uav-tracking-dataset) separately and follow its usage terms. Dataset files are not included in this repository.

The current lessons expect this layout (the repository folder can have any name):

```text
parent-folder/
|-- archive/
|   |-- Anti-UAV-Tracking-V0/
|   |   `-- video01/
|   |       `-- 00001.jpg
|   `-- Anti-UAV-Tracking-V0GT/
|       `-- video01_gt.txt
`-- repository-folder/
    |-- 01_hello.py
    |-- 02_open_image.py
    |-- 03_show_annotation.py
    `-- requirements.txt
```

Run a lesson from the repository folder:

```sh
python 01_hello.py
python 02_open_image.py
python 03_show_annotation.py
```

The image lessons open your system's image viewer. `python` must refer to your installed interpreter; select the appropriate interpreter in VS Code if needed.

The annotation is interpreted as `x y width height`. The red rectangle is a human-readable verification preview, not a model prediction or training input. Source images are unchanged.

## Local-only files

Personal VS Code settings, virtual environments, downloaded datasets, generated images, model files, and secrets are excluded by `.gitignore`. The local VS Code run tasks remain available on the original development computer.
