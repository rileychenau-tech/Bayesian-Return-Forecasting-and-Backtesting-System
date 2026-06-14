from src.data_loader import fetch_prices
from src.gbm_baseline import GBMBaseline
from src.plotter import plot_gbm_paths


def main():
    ticker = "SPY"
    start_date = "2020-01-01"

    # 1. Load historical prices
    prices = fetch_prices(ticker=ticker, start=start_date)

    # 2. Fit GBM baseline model
    model = GBMBaseline()
    model.fit(prices)

    # 3. Print estimated parameters
    print("\nGBM Baseline Parameters")
    print("-----------------------")
    print(f"Ticker: {ticker}")
    print(f"Annualised drift (mu): {model.params.mu:.4f}")
    print(f"Annualised volatility (sigma): {model.params.sigma:.4f}")

    # 4. Simulate future price paths
    paths = model.simulate_paths(
        start_price=prices.iloc[-1],
        days=252,
        n_paths=1000,
        seed=42
    )

    print("\nSimulation completed.")
    print(f"Simulated paths shape: {paths.shape}")

    # 5. Plot and save simulated paths
    plot_gbm_paths(
        paths=paths,
        ticker=ticker,
        save_path="outputs/figures/gbm_paths.png"
    )

    print("Figure saved to outputs/figures/gbm_paths.png")


if __name__ == "__main__":
    main()