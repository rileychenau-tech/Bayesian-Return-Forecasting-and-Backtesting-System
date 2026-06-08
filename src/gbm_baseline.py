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
    
    def simulate_paths(self, start_price, days=252, n_paths=1000, seed=42):
        if self.params is None:
            raise ValueError("Fit the model before simulating paths.")

        np.random.seed(seed)

        paths = np.zeros((days + 1, n_paths))
        paths[0] = start_price

        mu = self.params.mu
        sigma = self.params.sigma
        dt = self.params.dt

        for t in range(1, days + 1):
            random_shock = np.random.normal(0, 1, n_paths)
            paths[t] = paths[t - 1] * np.exp(
                (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * random_shock
            )

        return paths


# test
if __name__ == "__main__":
    import yfinance as yf

    prices = yf.download("SPY", start="2020-01-01")["Close"].squeeze()

    gbm = GBMBaseline()
    gbm.fit(prices)

    print(gbm.params)

    start_price = prices.iloc[-1]

    paths = gbm.simulate_paths(
        start_price=start_price,
        days=21,
        n_paths=5,
    )

    print("\nstarting price:", round(float(start_price), 2))
    print("paths shape:", paths.shape)
    print("simulated prices 21 days out:", paths[-1].round(2))