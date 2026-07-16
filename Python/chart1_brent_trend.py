"""
Chart 6 - Top 10 Currencies: Global Payment Share (Dec 2025, SWIFT)
"""
import matplotlib.pyplot as plt
from data_utils import get_currency_shares

shares = get_currency_shares().sort_values(ascending=True)

colors = []
for name in shares.index:
    if name == "USD":
        colors.append("#e8434f")
    elif name == "CNY":
        colors.append("#f4a259")
    else:
        colors.append("#9aa5ad")

fig, ax = plt.subplots(figsize=(9, 7))
bars = ax.barh(shares.index, shares.values, color=colors)

for bar, value in zip(bars, shares.values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f"{value:.2f}%", va="center", fontsize=10)

ax.set_title("Top 10 Currencies - Global Payment Share (Dec 2025, SWIFT)",
              fontsize=14, fontweight="bold")
ax.set_xlabel("Share (%)")
ax.set_xlim(0, shares.max() * 1.15)

from matplotlib.patches import Patch
legend_elems = [Patch(facecolor="#e8434f", label="USD"),
                Patch(facecolor="#f4a259", label="CNY/RMB"),
                Patch(facecolor="#9aa5ad", label="Other")]
ax.legend(handles=legend_elems, loc="lower right")

plt.tight_layout()
plt.savefig("chart6_currency_ranking.png", dpi=150)
plt.show()
