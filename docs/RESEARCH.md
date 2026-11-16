# Research and implementation references

- Ultralytics, YOLOv5 v7.0, commit 915bbf294bb74c859f0b41f1c23bc395014ea679. The retained CNN is a custom narrow adaptation with P2/P3 heads and ReLU. The vendor source and GPL license are included. https://github.com/ultralytics/yolov5/tree/v7.0
- Hobden, Srivastava, and Nurellari, FPGA-Based CNN for Real-Time UAV Tracking and Detection, 2022. Inspired combining motion processing with CNN observations. The project does not reproduce that architecture unchanged. https://doi.org/10.3389/frspt.2022.878010
- Zhang et al., ByteTrack, 2022. Informed the use of lower-confidence matched observations in the simplified software tracker. The R9 controller is not full ByteTrack. https://arxiv.org/abs/2110.06864
- Zhang et al., Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks, 2015. Background for computation reuse and memory-bandwidth tradeoffs. https://doi.org/10.1145/2684746.2689060
- dhm2013724/yolov2_xilinx_fpga. The CNN engine source credits channel/spatial tiling inspiration. Preserve its source comments and the original recorded provenance. https://github.com/dhm2013724/yolov2_xilinx_fpga
- Digilent, Genesys 2 reference documentation. Board pin mapping, device resources, clocks, and interfaces require the actual board constraints. https://digilent.com/reference/programmable-logic/genesys-2/start
- OmniVision, OV5640 Product Specification. Sensor timing and image-processing register reference. https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640_datasheet.pdf
- Espressif Systems, esp32-camera OV5640 driver and settings. Camera register recipe attribution and Apache license material are preserved. https://github.com/espressif/esp32-camera

Data sources are recorded in the training and validation manifests. The project used selections from DUT Anti-UAV, Anti-UAV300, the multi-sensor DroneDetectionThesis data, UAV-CB, ADE20K, and sky-background data. Obtain data from the authors under their own terms and retain the recorded split membership. Bulk images and videos are external to this repository.
