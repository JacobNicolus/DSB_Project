"""
Chart 7 - Offshore RMB Distribution by Economy (Dec 2025)
"""
import matplotlib.pyplot as plt
from data_utils import get_offshore_rmb_distribution

shares = get_offshore_rmb_distribution()

colors = ["#e8434f", "#c8c8c8", "#f4a259", "#4c78a8", "#2e7d5b", "#9fe0e0"]

fig, ax = plt.subplots(figsize=(9, 9))
ax.pie(
    shares.values,
    labels=shares.index,
    autopct="%.1f%%",
    colors=colors,
    startangle=90,
    counterclock=False,
    wedgeprops={"edgecolor": "white", "linewidth": 1},
)
ax.set_title("Offshore RMB Distribution by Economy (Dec 2025)", fontsize=15, fontweight="bold")
ax.axis("equal")

plt.tight_layout()
plt.savefig("chart7_offshore_rmb.png", dpi=150)
plt.show()
