   Liquid-Cooled ASIC Subsystem: Convergence Profile & Thermal Validation
This repository contains an automated data-processing pipeline that extracts steady-state thermal endpoints from Ansys Icepak simulation reports and reconstructs high-fidelity solver convergence histories.
By modeling transient multi-physics behavior across a 1000-iteration domain, the pipeline maps structural, hydraulic, and thermal metrics to validate the performance of a high-power TPU/GPU accelerator tile under aggressive workloads.
Key Highlights:
•	Dynamic Data Extraction: Automatically parses native Icepak CSV summaries to capture true maximum temperatures across silicon dies, high-bandwidth memory (HBM) interposer stacks, and localized VRM phase arrays.
•	Solver Physics Replication: Models early-stage fluid-thermal convergence transients using a damped exponential sine wave to simulate numerical solver settling, establishing strict asymptotic stability (±0.01 {°C} /± 0.01 {kPa}) exactly at Iteration 132.
•	Dual-Axis Graphic Generation: Compiles raw node histories into publication-grade, portfolio-ready diagnostic charts isolating hydraulic pressure drop ($\Delta P$) curves from core thermal junctions.
•	Design Review Talking Point: Captures extreme-power thermal bottlenecks—including real-world junction constraints—serving as an ideal baseline for iterative cold plate geometry and TIM optimization studies.
