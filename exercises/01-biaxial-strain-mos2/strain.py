from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Reference lattice parameters in Angstroms
a0 = 3.18

# Strain from -2% to +4%
strain = np.linspace(-0.02, 0.04, 61)

# Geometric model of biaxial strain 
a = a0 * (1 + strain)

# Display selected results
for i in range(0, len(strain), 10):
    print(
        f"Strain: {strain[i]*100:+.1f}% | "
        f"Lattice parameter: {a[i]:.4f} Å"
    )
    
# Plotting the results
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(
    strain * 100,
    a,
    linewidth=2,
    label="Biaxial strain model"
)

ax.set_xlabel("Biaxial strain (%)")
ax.set_ylabel("Lattice parameter (Å)")
ax.set_title("Biaxial Strain in Monolayer MoS2")


ax.grid(True, alpha=0.3)
ax.legend()

fig.tight_layout()

# Save the plot in the project's figures folder

# Locate the project directory
script_dir = Path(__file__).resolve().parent
project_dir = script_dir.parent.parent

# Create the figures directory if necessary
figures_dir = project_dir / "figures"
figures_dir.mkdir(parents=True, exist_ok=True)

# Save the figure
output_file = figures_dir / "mos2_biaxial_strain.png"

fig.savefig(output_file, dpi=300)

print(f"Figure saved successfully to: {output_file}")

plt.show()
