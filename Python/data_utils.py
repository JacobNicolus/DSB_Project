"""
Chart B3 - Correlation Heatmap: Brent Oil, Gold, Silver & USD/CNY (Monthly Returns)
"""
import matplotlib.pyplot as plt
import numpy as np
from data_utils import get_market_frame, get_usd_cny_series

df = get_market_frame()
usdcny = get_usd_cny_series().reindex(df.index).interpolate()
df["usd_cny"] = usdcny

returns = df.pct_change().dropna()
corr = returns.corr()

fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)

labels = ["Brent Oil", "Gold", "Silver", "USD/CNY"]
ax.set_xticks(range(len(labels)))
ax.set_yticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.set_yticklabels(labels)

for i in range(len(labels)):
    for j in range(len(labels)):
        ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center",
                 color="black", fontsize=10)

ax.set_title("Correlation Heatmap: Brent Oil, Gold, Silver & USD/CNY\n(Monthly Returns, 1994-2026)",
              fontsize=13, fontweight="bold")
fig.colorbar(im, ax=ax, label="Correlation Coefficient")

plt.tight_layout()
plt.savefig("chartB3_correlation_heatmap.png", dpi=150)
plt.show()
