"""
Chart 10 - USD/CNY Exchange Rate Trend (1994-2026)
"""
import matplotlib.pyplot as plt
import pandas as pd
from data_utils import get_usd_cny_series

series = get_usd_cny_series()

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(series.index, series.values, color="#2e7d5b", linewidth=2)
ax.fill_between(series.index, series.values, color="#2e7d5b", alpha=0.12)

d1 = pd.Timestamp("2005-07-01")
ax.axvline(d1, color="gray", linestyle="--", linewidth=0.8)
ax.annotate("2005\nDe-peg from\nUSD", xy=(d1, series.max() * 0.95),
            ha="center", fontsize=8, color="#555555")

d2 = pd.Timestamp("2015-08-01")
ax.axvline(d2, color="gray", linestyle="--", linewidth=0.8)
ax.annotate("2015\nRMB\nDevaluation", xy=(d2, series.max() * 0.85),
            ha="center", fontsize=8, color="#555555")

ax.set_title("USD/CNY Exchange Rate Trend (1994-2026)", fontsize=15, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("USD/CNY (RMB per US Dollar)")

plt.tight_layout()
plt.savefig("chart10_usd_cny_trend.png", dpi=150)
plt.show()
