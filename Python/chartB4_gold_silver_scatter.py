"""
Chart 4 - Gold vs Silver Price Comparison (1960-2026), dual y-axis
"""
import matplotlib.pyplot as plt
from data_utils import get_market_frame

df = get_market_frame()

fig, ax1 = plt.subplots(figsize=(11, 5.5))
ax2 = ax1.twinx()

l1, = ax1.plot(df.index, df["gold"], color="#f4a259", linewidth=2, label="Gold (left)")
l2, = ax2.plot(df.index, df["silver"], color="#4c78a8", linewidth=1.5, label="Silver (right)")

ax1.set_ylabel("Gold Price (USD/oz)", color="#f4a259")
ax2.set_ylabel("Silver Price (USD/oz)", color="#4c78a8")
ax1.tick_params(axis="y", labelcolor="#f4a259")
ax2.tick_params(axis="y", labelcolor="#4c78a8")
ax1.set_xlabel("Year")

ax1.set_title("Gold vs Silver Price Comparison (1960-2026)", fontsize=15, fontweight="bold")
ax1.legend(handles=[l1, l2], loc="upper left")

plt.tight_layout()
plt.savefig("chart4_gold_silver_combined.png", dpi=150)
plt.show()
