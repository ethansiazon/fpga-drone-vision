# External DDR3 simulation model

The historical full-MIG simulation runner expects ddr3_model.sv, ddr3_model_parameters.vh, and wiredly.v here. Obtain the matching Micron/MIG behavioral model under the provider's terms. These vendor simulation sources were excluded from the public migration because no redistribution license accompanied the local copies.

Vivado recreates the hardware MIG IP through bd/create_bd.tcl. The external model is needed for the corresponding behavioral simulation.
