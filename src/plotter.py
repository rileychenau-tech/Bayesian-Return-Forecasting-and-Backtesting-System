import os
import matplotlib.pyplot as plt


def plot_gbm_paths(paths, ticker: str, save_path: str):
    """Plot a sample of simulated GBM price paths and save the figure."""

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.figure(figsize=(10, 5))

    # paths shape: (days, n_paths)
    sample_paths = paths[:, :30]
    plt.plot(sample_paths)

    plt.title(f"GBM Simulated Price Paths for {ticker}")
    plt.xlabel("Trading Days")
    plt.ylabel("Simulated Price")
    plt.tight_layout()

    plt.savefig(save_path, dpi=300)
    plt.close()