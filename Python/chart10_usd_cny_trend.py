"""
Chart 2 - Gold Prices (1960-2026): Long-Term Trend & Safe-Haven Behaviour
"""
import matplotlib.pyplot as plt
import pandas as pd
from data_utils import get_market_frame, EVENTS_GOLD

df = get_market_frame()

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(df.index, df["gold"], color="#f4a259", linewidth=2)
ax.fill_between(df.index, df["gold"], color="#f4a259", alpha=0.12)

for date_str, label in EVENTS_GOLD.items():
    date = pd.Timestamp(date_str)
    if df.index.min() <= date <= df.index.max():
        ax.axvline(date, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
        ax.annotate(label, xy=(date, df["gold"].max() * 0.85), ha="center",
                    fontsize=8, color="#555555")

ax.set_title("Gold Prices (1960-2026) - Long-Term Trend & Safe-Haven Behaviour",
              fontsize=15, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Price (USD per troy oz)")
ax.set_ylim(bottom=0)

plt.tight_layout()
plt.savefig("chart2_gold_trend.png", dpi=150)
plt.show()
