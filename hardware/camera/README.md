# OV5640 R13 camera

The frozen source in r13/ matches the preferred 20 FPS majority-filter build. Its RTL and constraints are byte-identical to the saved source snapshot. Host scripts and simulation entry points were relocated for this repository.

Read [WIRING.md](WIRING.md). PCLK is JA physical pin 1 and D6 is JB physical pin 8. The module labels its 8-bit data bus D2 through D9. Verify the actual wiring before programming.

Normal live viewing uses only SW6 up, with the other switches down, followed by BTNC and a settling interval. SW5 selects FPGA-generated bars. SW1 selects camera-generated bars. SW7 triggers the recorder. A clean camera-generated pattern does not establish correct colour in a real scene.

## Saved camera bitstream

Use [artifacts/camera/r13](../../artifacts/camera/r13) for the matching camera-only binary and reports. The camera uses 320 × 240 RGB565 with approximately 20 camera FPS. HDMI refreshes 640 × 480 at 60 Hz. This camera-only build is separate from the live-camera CNN rev-3 artifact.

## Offline checks

Install Icarus Verilog and make iverilog/vvp available on PATH, or pass their executable paths.

```powershell
python tools/test_camera.py --out local_results/camera_check --only tb_yuv_capture_qualified tb_top_reference_readout_20fps_filter
```

The top-level functional fixture substitutes clock/HDMI primitives. It checks receiver behavior and injected short glitches, with physical timing and image appearance covered by separate evidence.

## Create or build a fresh camera project

In Vivado Tcl, from the repository root.

```tcl
set argv [list C:/g2_r13_project]
source tools/create_camera_project.tcl
```

The default format is RGB565 and the default readout is reference2x-20fps-filter. The project creation script refuses an existing output directory.

The bounded build entry point preserves the free-memory guard and refuses another active batch compiler.

```powershell
python -m pip install psutil==5.9.8
python tools/build_camera_guarded.py --vivado C:/AMDDesignTools/2026.1/Vivado/bin/vivado.bat --out builds/r13_rebuild
```

## Live UART image controls

After intentionally loading the camera-only R13 build, USB-UART J15 supports the existing camera commands. Run the tuner with the current serial port.

```powershell
powershell -ExecutionPolicy Bypass -File hardware/camera/r13/scripts/tune_r13.ps1 -Port COM3
```

Commands include `show`, `exposure 400`, `gain 1.25`, `wb auto`, `wb hold`, `brightness 1`, `contrast 1`, `saturation 1`, `undo`, and `save my_pick`. Use `help` for the full list. Saved settings remain local under local_results/. Board reset restores startup settings.

The integrated rev-3 build documents its own H/A white-balance commands. Its serial protocol has not been established as compatible with this full camera-only tuner. Confirm the loaded build before using an adjustment tool.
