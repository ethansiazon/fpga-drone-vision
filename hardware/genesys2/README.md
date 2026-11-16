# Genesys 2 board implementation

reference_oct29/ preserves Niko Warren's October 29 standalone DDR3/CNN/decoder implementation, its generated cores, block-design Tcl, constraints, scripts, and saved reports. It accepts prepared image input and predates the shipped November camera integration.

The root paths of that source are calculated relative to its own scripts. Keeping this subtree together preserves the reference layout. Historical Linux tool locations in shell runners need adaptation for another machine. Read its HANDOFF.md, PHASE1_STATUS.md, PHASE2_STATUS.md, and docs/PHASE2_LOG.md as historical records.

The original board implementation uses Vivado 2023.2 and the Genesys 2 board definition. Vendor IP such as MIG, SmartConnect, clocking, and AXI clock converters is recreated by Vivado from bd/create_bd.tcl. Build scripts can launch substantial compiler work and are not run during repository verification.

The Micron DDR3 behavioral simulation files were omitted from this public distribution because the supplied copies include copyright notices without a redistribution license. Obtain the appropriate model through the vendor tooling or provider under its terms before using the full-MIG simulation runner. The expected model filenames remain documented in sim/mig_sim_models/README.md.

The later live-camera binary is in artifacts/genesys2/live_camera_rev3. Its matching source is missing here. Rebuilding reference_oct29 does not reproduce that later binary.
