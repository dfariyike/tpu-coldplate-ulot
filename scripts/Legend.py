import matplotlib.pyplot as plt
import matplotlib as mpl

# Set up a clean, high-resolution figure size
fig, ax = plt.subplots(figsize=(1.8, 7))
fig.subplots_adjust(right=0.45)

# Use 'jet' or 'turbo' to perfectly mirror standard CFD visual profiles
cmap = mpl.cm.jet 
norm = mpl.colors.Normalize(vmin=35.0, vmax=105.0)

cb = mpl.colorbar.ColorbarBase(ax, cmap=cmap, norm=norm, orientation='vertical')
cb.set_label('Surface Temperature (°C)', fontsize=12, fontweight='bold', labelpad=10)

# Define your exact target presentation data points
ticks = [35.0, 41.2, 60.0, 81.5, 82.5, 102.4, 105.0]

# Structure the labels cleanly to prevent any text overlapping
labels = [
    '35.0 (Inlet)', 
    '41.2 (Outlet)', 
    '60.0', 
    '81.5 (HBM)', 
    '82.5 (TPU)', 
    '102.4 (VRM 4 Hotspot)', 
    '105.0'
]

cb.set_ticks(ticks)
cb.set_ticklabels(labels)

# Minor formatting tweak: cleanly realign the specific overlapping ticks if needed
for t in ax.yaxis.get_major_ticks():
    t.label1.set_fontsize(10)
    t.label1.set_fontweight('medium')

# Save the polished asset
plt.savefig("final_presentation_legend.png", dpi=300, bbox_inches='tight')
print("Custom legend generated successfully!")