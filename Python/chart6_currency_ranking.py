"""
Chart 5 - Brent Crude Oil Annual Average Prices (Bar Chart, 1960-2026)
"""
import matplotlib.pyplot as plt
from data_utils import get_market_frame

df = get_market_frame()
annual = df["brent"].resample("YS").mean()

fig, ax = plt.subplots(figsize=(12, 5.5))
colors = plt.cm.autumn_r((annual - annual.min()) / (annual.max() - annual.min()))
ax.bar(annual.index.year, annual.values, color=colors, width=0.8)

ax.set_title("Brent Crude Oil - Annual Average Prices (1960-2026)", fontsize=15, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Average Price (USD per barrel)")
ax.set_xticks(range(1960, 2027, 5))

plt.tight_layout()
plt.savefig("chart5_brent_annual_bar.png", dpi=150)
plt.show()
