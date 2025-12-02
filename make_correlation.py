# make_correlation.py
# Generates synthetic supply-chain data, correlation.csv, and a heatmap image
# Author: Rahul Kumar
# Email: 24f2001869@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Create synthetic supply-chain dataset (51 samples)
n = 51
data = pd.DataFrame({
    "Supplier_Lead_Time": np.clip(np.random.normal(10, 3, n), 1, 30),
    "Inventory_Levels": np.clip(np.random.normal(500, 200, n), 10, 5000),
    "Order_Frequency": np.clip(np.random.poisson(4, n), 1, 30),
    "Delivery_Performance": np.clip(0.8 + np.random.normal(0, 0.05, n), 0.4, 1.0),
    "Cost_Per_Unit": np.clip(np.random.normal(50, 15, n), 1, 500)
})

# Introduce some realistic relationships (so correlations look meaningful)
# Higher lead time -> slightly worse delivery performance
data["Delivery_Performance"] -= (data["Supplier_Lead_Time"] - data["Supplier_Lead_Time"].mean()) * 0.003
# Higher inventory where order frequency is low (inverse)
data["Inventory_Levels"] += (5 - data["Order_Frequency"]) * 30
# Cost and delivery performance weakly related
data["Cost_Per_Unit"] += (1 - data["Delivery_Performance"]) * 5

# Compute correlation matrix
corr = data.corr()

# Save CSV
corr.to_csv("correlation.csv", float_format="%.4f")

# Create red-white-green heatmap
plt.figure(figsize=(4.5, 4.5), dpi=100)  # 4.5in * 100dpi = 450px
cmap = sns.diverging_palette(10, 240, sep=60, as_cmap=True)  # red-white-green style
sns.heatmap(corr, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1, square=True,
            cbar_kws={"shrink": 0.75})
plt.title("Correlation Matrix — Supply Chain Metrics", pad=12)
plt.tight_layout()
plt.savefig("heatmap.png", dpi=100, bbox_inches="tight")  # final image ~450x450 px
plt.close()

# Also save the synthetic dataset for transparency (optional)
data.to_csv("supplychain_data.csv", index=False, float_format="%.4f")

print("Saved: correlation.csv, heatmap.png, supplychain_data.csv")
