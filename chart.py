# chart.py
# Generates a Seaborn scatterplot for Customer LTV vs Acquisition Cost
# Saves chart.png at 512x512 px
# Author: Rahul Kumar
# Email: 24f2001869@ds.study.iitm.ac.in

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(123)

# Generate synthetic customer cohort data (realistic-ish)
n = 600
acquisition_cost = np.random.gamma(shape=2.0, scale=30.0, size=n) + np.random.normal(0, 5, n)
# Lifetime value positively correlated with cost but with variance
ltv = acquisition_cost * (np.random.normal(3.5, 0.8, n)) + np.random.normal(0, 200, n)
# Cap/clean
acquisition_cost = np.clip(acquisition_cost, 5, 1000)
ltv = np.clip(ltv, 50, 20000)

df = pd.DataFrame({
    "Acquisition_Cost": acquisition_cost,
    "Customer_LTV": ltv,
    "Segment": np.random.choice(["Retail", "SMB", "Enterprise"], size=n, p=[0.6, 0.3, 0.1])
})

# Styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)
palette = {"Retail":"#1f77b4", "SMB":"#ff7f0e", "Enterprise":"#2ca02c"}

plt.figure(figsize=(8, 8), dpi=64)  # 8in * 64dpi = 512 px
ax = sns.scatterplot(data=df, x="Acquisition_Cost", y="Customer_LTV", hue="Segment",
                     palette=palette, alpha=0.75, edgecolor="w", linewidth=0.4, s=70)

# Fit a regression line (overall)
sns.regplot(data=df, x="Acquisition_Cost", y="Customer_LTV",
            scatter=False, ax=ax, line_kws={"color":"black", "lw":1.2, "alpha":0.6})

ax.set_title("Customer Lifetime Value vs Acquisition Cost", pad=14)
ax.set_xlabel("Acquisition Cost (USD)")
ax.set_ylabel("Customer Lifetime Value (USD)")
ax.legend(title="Segment", loc="upper left")
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 512x512 px
plt.close()

print("Saved: chart.png")
