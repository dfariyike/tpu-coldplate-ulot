import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the generated simulation monitor log
csv_filename = "monitor_point_history.csv"
df = pd.read_csv(csv_filename)

# 2. Setup the visualization canvas (Subplots for clean separation)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8.5))

# ---------------------------------------------------------
# PLOT 1: THERMAL PERFORMANCE & STABILIZATION PROFILE
# ---------------------------------------------------------
# Plot the primary thermal hotspots and profiles
ax1.plot(df['Iteration'], df['VRM 4 Monitor Point Temperature (°C)'], 
         label='VRM 4 (Hotspot Max)', color='#d62728', linewidth=1.5)
ax1.plot(df['Iteration'], df['VRM 2 Monitor Point Temperature (°C)'], 
         label='VRM 2 (Standard Phase)', color='#bcbd22', linestyle='--')
ax1.plot(df['Iteration'], df['TPU Monitor Point Temperature (°C)'], 
         label='TPU Silicon Core', color='#ff7f0e', linewidth=2)

# Compute and plot an aggregate HBM trend for clean presentation visual
hbm_cols = [f'HBM {i} Monitor Point Temperature (°C)' for i in range(1, 9)]
df['HBM_Average'] = df[hbm_cols].mean(axis=1)
ax1.plot(df['Iteration'], df['HBM_Average'], 
         label='HBM Core Array (Avg)', color='#e377c2', linestyle='-.')

ax1.plot(df['Iteration'], df['Outlet Monitor Point Temperature (°C)'], 
         label='Liquid Coolant Outlet', color='#1f77b4', linewidth=1.5)

# Formatting Plot 1
ax1.set_title("Liquid-Cooled ASIC Assembly: Thermal Convergence History", fontsize=13, fontweight='bold', pad=12)
ax1.set_ylabel("Temperature (°C)", fontsize=11, fontweight='bold')
ax1.set_xlim(0, 1000)
ax1.set_ylim(15, 115)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')

# Add explicit engineering annotation callout at Iteration 132
ax1.annotate('Solver Convergence\n(Iteration 132 Overlock)', xy=(132, 82.5), 
             xytext=(260, 60), fontweight='bold', color='#222222', fontsize=9,
             arrowprops=dict(facecolor='#333333', shrink=0.08, width=1.2, headwidth=6))

# ---------------------------------------------------------
# PLOT 2: HYDRAULIC PERFORMANCE & PRESSURE DROP
# ---------------------------------------------------------
# Convert raw Pascals (N/m²) to kPa for standardized dashboard representation
df['Inlet_kPa'] = df['Inlet Monitor Point Pressure (N/m2)'] / 1000
df['Outlet_kPa'] = df['Outlet Monitor Point Pressure (N/m2)'] / 1000
df['System_DeltaP_kPa'] = df['Inlet_kPa'] - df['Outlet_kPa']

ax2.plot(df['Iteration'], df['Inlet_kPa'], label='Inlet Loop Pressure', color='#2ca02c', linewidth=1.5)
ax2.plot(df['Iteration'], df['Outlet_kPa'], label='Outlet Return Pressure', color='#9467bd', linewidth=1.5)
ax2.plot(df['Iteration'], df['System_DeltaP_kPa'], label='Total System Resistance (ΔP)', 
         color='#7f7f7f', linestyle=':', linewidth=2)

# Formatting Plot 2
ax2.set_title("Cold Plate Hydraulic Impedance Profile", fontsize=13, fontweight='bold', pad=12)
ax2.set_xlabel("ANSYS Icepak Solver Iterations", fontsize=11, fontweight='bold')
ax2.set_ylabel("Hydraulic Pressure (kPa)", fontsize=11, fontweight='bold')
ax2.set_xlim(0, 1000)
ax2.set_ylim(0, 45)
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='none')

# 3. Finalize and Save Graphic Layout
plt.tight_layout()
plt.savefig("vrm_tpu_cooling_dashboard.png", dpi=300)
print("Post-processing complete. 'vrm_tpu_cooling_dashboard.png' has been saved successfully.")