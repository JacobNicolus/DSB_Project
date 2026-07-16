"""
Chart 11 - Global Commodity & Currency Market Dashboard (1960-2026)
2x2 dark-themed dashboard: Brent, Gold, Silver trends + currency share bar chart.
"""
import matplotlib.pyplot as plt
from data_utils import get_market_frame, get_currency_shares

df = get_market_frame()
shares = get_currency_shares().sort_values(ascending=True).tail(6)

plt.style.use("dark_background")
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.patch.set_facecolor("#0d1b2a")

# Brent
ax = axes[0, 0]
ax.plot(df.index, df["brent"], color="#e8434f", linewidth=1.8)
ax.fill_between(df.index, df["brent"], color="#e8434f", alpha=0.15)
ax.set_title("Brent Crude Oil", fontweight="bold")
ax.set_ylabel("USD/bbl")

# Gold
ax = axes[0, 1]
ax.plot(df.index, df["gold"], color="#f4a259", linewidth=1.8)
ax.fill_between(df.index, df["gold"], color="#f4a259", alpha=0.15)
ax.set_title("Gold", fontweight="bold")
ax.set_ylabel("USD/oz")

# Silver
ax = axes[1, 0]
ax.plot(df.index, df["silver"], color="#4c78a8", linewidth=1.8)
ax.fill_between(df.index, df["silver"], color="#4c78a8", alpha=0.15)
ax.set_title("Silver", fontweight="bold")
ax.set_ylabel("USD/oz")

# Currency shares
ax = axes[1, 1]
colors = ["#e8434f" if n == "USD" else ("#f4a259" if n == "CNY" else "#9aa5ad")
          for n in shares.index]
ax.barh(shares.index, shares.values, color=colors)
ax.set_title("Top Currency Payment Shares (Dec 2025)", fontweight="bold")
ax.set_xlabel("Share (%)")

fig.suptitle("Global Commodity & Currency Market Dashboard  |  1960-2026",
             fontsize=17, fontweight="bold", color="white")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("chart11_dashboard.png", dpi=150, facecolor=fig.get_facecolor())
plt.show()
