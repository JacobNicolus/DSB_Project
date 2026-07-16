"""
Chart 9 - Monthly Price Volatility: Brent Oil vs Gold vs Silver (1960-2026)
Three stacked panels, month-over-month % change, gains vs losses color coded.
"""
import matplotlib.pyplot as plt
from data_utils import get_market_frame

df = get_market_frame()
pct = df.pct_change().dropna() * 100

fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
panels = [
    ("brent", "Brent Oil Monthly % Change", "#e8434f"),
    ("gold", "Gold Monthly % Change", "#f4a259"),
    ("silver", "Silver Monthly % Change", "#4c78a8"),
]

for ax, (col, title, color) in zip(axes, panels):
    values = pct[col]
    colors = [color if v >= 0 else "#9aa5ad" for v in values]
    ax.bar(values.index, values.values, color=colors, width=20)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_ylabel("MoM % Change")

axes[-1].set_xlabel("Year")
fig.suptitle("Monthly Price Volatility: Brent Oil vs Gold vs Silver (1960-2026)",
             fontsize=15, fontweight="bold", y=1.0)

plt.tight_layout()
plt.savefig("chart9_monthly_volatility.png", dpi=150)
plt.show()
