"""
data_utils.py
-------------
Shared helper module for the Global Commodity & Currency Market Research report.

Builds monthly time series (1960-2026) for Brent Crude Oil, Gold, and Silver
by interpolating between well-known historical benchmark prices and adding
realistic month-to-month noise. Also provides the small static tables used
for the currency-share and offshore-RMB charts.

NOTE: These series are reconstructed approximations for report/chart-building
purposes (anchored on well-documented historical price levels), not an
official data feed. Replace `load_real_data()` with a call to your own
CSV/Excel/Refinitiv/World-Bank pull if you have the original source file.
"""

import numpy as np
import pandas as pd


def _build_series(anchor_dates, anchor_prices, freq="MS", noise_pct=0.03, seed=1):
    """Interpolate anchor points onto a monthly index and add smooth noise."""
    anchors = pd.Series(anchor_prices, index=pd.to_datetime(anchor_dates))
    full_index = pd.date_range(anchors.index.min(), anchors.index.max(), freq=freq)
    series = anchors.reindex(full_index)
    series = series.interpolate(method="pchip").clip(lower=0.01)

    rng = np.random.default_rng(seed)
    noise = rng.normal(loc=0, scale=noise_pct, size=len(series))
    # smooth the noise a little so months aren't independent random jumps
    noise = pd.Series(noise, index=series.index).rolling(3, min_periods=1).mean()
    series = series * (1 + noise)
    return series.round(2)


def get_brent_series():
    dates = ["1960-01-01", "1973-09-01", "1974-01-01", "1979-06-01", "1980-06-01",
              "1986-01-01", "1986-06-01", "1990-06-01", "1990-10-01", "1993-01-01",
              "1999-01-01", "2000-09-01", "2004-01-01", "2008-07-01", "2008-12-01",
              "2011-04-01", "2012-03-01", "2014-06-01", "2016-01-01", "2018-10-01",
              "2020-04-01", "2021-06-01", "2022-06-01", "2023-06-01", "2025-01-01",
              "2026-06-01"]
    prices = [1.6, 3, 11, 15, 40, 27, 10, 17, 34, 17, 10, 33, 30, 133, 42,
              123, 125, 108, 30, 80, 24, 73, 120, 76, 72, 121]
    return _build_series(dates, prices, noise_pct=0.05, seed=10)


def get_gold_series():
    dates = ["1960-01-01", "1971-08-01", "1974-01-01", "1979-01-01", "1980-01-01",
              "1982-01-01", "1987-01-01", "1996-01-01", "2001-01-01", "2005-01-01",
              "2008-10-01", "2011-09-01", "2012-10-01", "2015-12-01", "2018-08-01",
              "2020-08-01", "2022-09-01", "2024-01-01", "2024-10-01", "2026-06-01"]
    prices = [35, 43, 155, 500, 675, 375, 480, 390, 270, 445, 730, 1780, 1750, 1060,
               1195, 2000, 1650, 2050, 2700, 5030]
    return _build_series(dates, prices, noise_pct=0.03, seed=20)


def get_silver_series():
    dates = ["1960-01-01", "1974-01-01", "1979-06-01", "1980-01-01", "1980-06-01",
              "1982-06-01", "1987-01-01", "1993-01-01", "2001-01-01", "2006-01-01",
              "2008-10-01", "2011-04-01", "2013-06-01", "2015-12-01", "2020-03-01",
              "2021-02-01", "2022-09-01", "2024-01-01", "2025-06-01", "2026-06-01"]
    prices = [0.9, 5, 8, 39, 16, 6, 7, 3.7, 4.4, 10.5, 9, 42, 21, 14, 12,
               27, 19, 24, 34, 92]
    return _build_series(dates, prices, noise_pct=0.06, seed=30)


def get_usd_cny_series():
    dates = ["1994-01-01", "2005-07-01", "2008-01-01", "2014-01-01", "2016-01-01",
              "2018-06-01", "2020-05-01", "2022-10-01", "2024-01-01", "2026-06-01"]
    rates = [8.7, 8.1, 6.83, 6.05, 6.95, 6.4, 7.1, 7.3, 7.2, 7.1]
    return _build_series(dates, rates, noise_pct=0.01, seed=40)


def get_market_frame():
    """Combine Brent / Gold / Silver into one aligned monthly DataFrame (1960-2026)."""
    brent = get_brent_series()
    gold = get_gold_series()
    silver = get_silver_series()
    df = pd.DataFrame({"brent": brent, "gold": gold, "silver": silver})
    df = df.dropna()
    return df


# ---- Static tables (SWIFT payment shares & offshore RMB distribution) ----
# Source context: SWIFT RMB Tracker style summary, Dec-2025 snapshot used in the report.

def get_currency_shares():
    data = {
        "USD": 50.49, "EUR": 21.90, "GBP": 6.73, "CAD": 3.44, "JPY": 3.42,
        "CNY": 2.73, "HKD": 1.68, "AUD": 1.60, "SGD": 1.33, "CHF": 0.95,
    }
    return pd.Series(data, name="share_pct")


def get_offshore_rmb_distribution():
    data = {
        "Hong Kong": 75.9, "Others": 7.7, "United Kingdom": 7.2,
        "Singapore": 4.5, "France": 2.7, "United States": 2.0,
    }
    return pd.Series(data, name="share_pct")


EVENTS_BRENT = {
    "1973-10-01": "1973\nOPEC\nEmbargo",
    "1980-01-01": "1980\nIran-Iraq\nWar",
    "1986-01-01": "1986\nPrice\nCollapse",
    "1990-08-01": "1990\nGulf\nWar",
    "2008-07-01": "2008\nPeak",
    "2014-06-01": "2014\nShale\nGlut",
    "2020-03-01": "2020\nCOVID",
    "2022-02-01": "2022\nUkraine\nWar",
}

EVENTS_GOLD = {
    "1971-08-01": "1971\nNixon Shock",
    "1980-01-01": "1980\nPeak",
    "2008-10-01": "2008\nGFC",
    "2011-09-01": "2011\nPeak",
    "2020-08-01": "2020\nCOVID",
    "2022-03-01": "2022\nUkraine",
    "2024-10-01": "2024\nAll-Time\nHigh",
}

EVENTS_SILVER = {
    "1980-01-01": "1980\nHunt\nBrothers",
    "2008-10-01": "2008\nGFC",
    "2011-04-01": "2011\nPeak",
    "2020-03-01": "2020\nCOVID",
    "2021-02-01": "2021\nMeme\nSqueeze",
}
