import numpy as np
import pandas as pd
import yfinance as yf


def fetch_prices(ticker: str = "NDQ.AX",
                 start: str = "2020-01-01",
                 end: str | None = None) -> pd.Series:
    """Download adjusted close prices."""
    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No data found for {ticker}.")

    prices = data["Close"].dropna().squeeze()
    prices.name = ticker

    if len(prices) < 2:
        raise ValueError("Not enough price data.")

    print(f"[data] loaded {len(prices)} daily prices for {ticker}")

    return prices


def compute_log_returns(prices: pd.Series) -> pd.Series:
    """Compute daily log returns from prices."""
    log_returns = np.log(prices / prices.shift(1)).dropna()
    log_returns.name = "log_return"

    return log_returns


def load_market_data(ticker: str = "NDQ.AX",
                     start: str = "2020-01-01",
                     end: str | None = None):
    """Load prices and log returns together."""
    prices = fetch_prices(ticker=ticker, start=start, end=end)
    log_returns = compute_log_returns(prices)

    print(f"[data] calculated {len(log_returns)} daily log returns")

    return prices, log_returns


# quick test
if __name__ == "__main__":
    prices, log_returns = load_market_data("NDQ.AX", start="2020-01-01")

    print("\nprices:")
    print(prices.head())

    print("\nlog returns:")
    print(log_returns.head())