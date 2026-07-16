"""
Chart B5 - Gold Price with 12-Month and 60-Month Moving Averages (1960-2026)
"""
import matplotlib.pyplot as plt
from data_utils import get_market_frame

df = get_market_frame()
gold = df["gold"]
ma12 = gold.rolling(12).mean()
ma60 = gold.rolling(60).mean()

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(gold.index, gold.values, color="#c9c9c9", linewidth=1, label="Gold (monthly)")
ax.plot(ma12.index, ma12.values, color="#f4a259", linewidth=2, label="12-Month Moving Avg")
ax.plot(ma60.index, ma60.values, color="#8b3a3a", linewidth=2, label="60-Month Moving Avg")

ax.set_title("Gold Price with Moving Averages (1960-2026)", fontsize=15, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Price (USD per troy oz)")
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("chartB5_gold_moving_avg.png", dpi=150)
plt.show()
