# Supply Chain Correlation & Seaborn Visuals

Contact: 24f2001869@ds.study.iitm.ac.in

This repository contains:
- `correlation.csv` — correlation matrix for supply chain metrics.
- `heatmap.png` — 450×450 px heatmap of the correlation matrix (Red-White-Green).
- `chart.py` — Seaborn script producing `chart.png` (512×512 px).
- `chart.png` — Generated scatterplot (Customer LTV vs Acquisition Cost).

Usage:
- To regenerate correlation files and images run: `python make_correlation.py`
- To regenerate the seaborn chart run: `python chart.py`
