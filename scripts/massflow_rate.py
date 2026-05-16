# Quick thermodynamic validation for your dashboard back-end
Q_total = 490.4  # Total Watts from your summary report file
mass_flow_rate = 0.015  # Extracted mass flow rate in kg/s
Cp_water = 4184  # Specific heat capacity of water J/(kg*C)

# Calculate bulk fluid temperature rise
delta_T_fluid = Q_total / (mass_flow_rate * Cp_water)
print(f"Calculated Fluid Temperature Rise: {delta_T_fluid:.2f}°C")