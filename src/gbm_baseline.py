import numpy as np
import pandas as pd
from dataclasses import dataclass


@dataclass
class GBMParams:
    mu: float  # annualised drift
    sigma: float  # annualised volatility
    dt: float = 1/252


class GBMBaseline:
    def __init__(self):
        self.params = None

    def fit(self, prices: pd.Series) -> "GBMBaseline":
        log_returns = np.log(prices / prices.shift(1)).dropna()

        daily_mu    = log_returns.mean()
        daily_sigma = log_returns.std()

        sigma_ann   = daily_sigma * np.sqrt(252)
        mu_ann      = daily_mu * 252 + 0.5 * sigma_ann**2

        self.params = GBMParams(mu=mu_ann, sigma=sigma_ann)
        return self


# test
if __name__ == "__main__":
    import yfinance as yf
    prices = yf.download("SPY", start="2020-01-01")["Close"].squeeze()
    gbm = GBMBaseline().fit(prices)
    print(gbm.params)