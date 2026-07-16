"""
Chart B6 - Brent Crude Oil - Linear Trendline Forecast (Estimate Only, Not a Prediction)
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from data_utils import get_market_frame

df = get_market_frame()
hist = df["brent"].loc["2000-01-01":]

# Fit a simple linear trend on the last 24 months to project forward 24 months
recent = hist.iloc[-24:]
x_recent = np.arange(len(recent))
coeffs = np.polyfit(x_recent, recent.values, 1)

future_periods = 24
future_dates = pd.date_range(hist.index[-1], periods=future_periods + 1, freq="MS")[1:]
x_future = np.arange(len(recent), len(recent) + future_periods)
forecast = np.polyval(coeffs, x_future)
uncertainty = 15  # +/- $15 band, matches report annotation

fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(hist.index, hist.values, color="#e8434f", linewidth=1.8, label="Historical Brent Oil")
ax.plot(future_dates, forecast, color="navy", linewidth=2.2, linestyle="--",
        label="Linear Forecast (estimate only)")
ax.fill_between(future_dates, forecast - uncertainty, forecast + uncertainty,
                 color="navy", alpha=0.15, label=f"Uncertainty Band (\u00b1${uncertainty})")
ax.axvline(hist.index[-1], color="gray", linestyle=":", linewidth=1)

ax.set_title("Brent Crude Oil - Linear Trendline Forecast (Estimate Only, Not a Prediction)",
              fontsize=13, fontweight="bold")
ax.set_xlabel("Year")
ax.set_ylabel("Price (USD/bbl)")
ax.legend(loc="upper left")

ax.text(0.02, 0.05,
        "\u26a0 Forecast is a simple linear estimate only.\n"
        "Actual prices depend on geopolitical, supply, and demand factors.",
        transform=ax.transAxes, fontsize=9, style="italic",
        bbox=dict(boxstyle="round", facecolor="#fff9c4", edgecolor="#cccccc"))

plt.tight_layout()
plt.savefig("chartB6_brent_forecast.png", dpi=150)
plt.show()
