"""
Chart 1 - Brent Crude Oil Prices (1960-2026) with Major Events
Recreates: "Brent Crude Oil Prices (1960-2026) with Major Events"
"""
import matplotlib.pyplot as plt
import pandas as pd
from data_utils import get_market_frame, EVENTS_BRENT

df = get_market_frame()

plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
fig, ax = plt.subplots(figsize=(11, 5.5))

ax.plot(df.index, df["brent"], color="#e8434f", linewidth=2, label="Brent Crude ($/bbl)")
ax.fill_between(df.index, df["brent"], color="#e8434f", alpha=0.12)

for date_str, label in EVENTS_BRENT.items():
    date = pd.Timestamp(date_str)
    if df.index.min() <= date <= df.index.max():
        ax.axvline(date, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
        ax.annotate(label, xy=(date, df["brent"].max() * 0.85),
                    ha="center", fontsize=8, color="#555555")

ax.set_title("Brent Crude Oil Prices (1960-2026) with Major Events", fontsize=15, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Price (USD per barrel)")
ax.legend(loc="upper left")
ax.set_ylim(bottom=0)

plt.tight_layout()
plt.savefig("chart1_brent_trend.png", dpi=150)
plt.show()
