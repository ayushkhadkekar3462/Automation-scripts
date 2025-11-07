import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

path = "pvsyst_outputs/"
files = glob.glob(os.path.join(path, "*.csv"))

results = []
for file in files:
    df = pd.read_csv(file)
    energy = df["E_Grid"].sum()
    pr = df["PR"].mean()
    name = os.path.splitext(os.path.basename(file))[0]
    tilt = int(name.split("_")[1].replace("tilt", ""))
    azimuth = int(name.split("_")[2].replace("az", ""))
    results.append({"Configuration": name, "Tilt": tilt, "Azimuth": azimuth, "Energy (MWh)": energy, "PR (%)": pr * 100})

data = pd.DataFrame(results)
best = data.loc[data["Energy (MWh)"].idxmax()]

plt.figure(figsize=(10, 6))
plt.bar(data["Configuration"], data["Energy (MWh)"])
plt.xticks(rotation=45, ha="right")
plt.title("Annual Energy Yield Comparison of PV Configurations")
plt.xlabel("Configuration")
plt.ylabel("Energy Yield (MWh)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(data["Tilt"], data["Azimuth"], s=data["Energy (MWh)"], c=data["PR (%)"], cmap="viridis", edgecolor="black")
plt.colorbar(label="Performance Ratio (%)")
plt.title("Performance Landscape of PV Configurations")
plt.xlabel("Tilt (°)")
plt.ylabel("Azimuth (°)")
plt.tight_layout()
plt.show()

print("Best Configuration:")
print(best)
