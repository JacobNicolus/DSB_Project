"""
Chart B4 - Gold vs Silver Annual Average Prices - Scatter Plot (1960-2026)
Includes a linear trendline and R^2 value.
"""
import matplotlib.pyplot as plt
import numpy as np
from data_utils import get_market_frame

df = get_market_frame()
annual = df.resample("YS").mean()

x = annual["gold"].values
y = annual["silver"].values
years = annual.index.year

# Linear trendline
coeffs = np.polyfit(x, y, 1)
trend_x = np.array([x.min(), x.max()])
trend_y = np.polyval(coeffs, trend_x)
y_pred = np.polyval(coeffs, x)
ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - y.mean()) ** 2)
r_squared = 1 - ss_res / ss_tot

fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(x, y, c=years, cmap="plasma", edgecolors="white", s=60, alpha=0.9)
ax.plot(trend_x, trend_y, color="red", linewidth=2, label=f"Trendline  R\u00b2={r_squared:.3f}")

ax.set_title("Gold vs Silver Annual Average Prices - Scatter Plot (1960-2026)",
              fontsize=14, fontweight="bold")
ax.set_xlabel("Gold Price (USD/oz)")
ax.set_ylabel("Silver Price (USD/oz)")
ax.legend(loc="upper left")

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label("Year")

plt.tight_layout()
plt.savefig("chartB4_gold_silver_scatter.png", dpi=150)
plt.show()
