# Bayesian Return Forecasting and Backtesting System

This project is a quantitative finance project designed to build the foundation for a Bayesian return forecasting and backtesting system.

The current version implements a **Geometric Brownian Motion (GBM) baseline model** using historical market data. It loads real stock price data, estimates annualised drift and volatility from log returns, simulates future price paths using Monte Carlo simulation, and saves a visual output of simulated GBM paths.

This baseline version will later be extended into a Bayesian forecasting system, where prior beliefs about return and volatility are updated using new market data to generate posterior return forecasts and uncertainty estimates.

---

## Project Motivation

Financial markets are uncertain and constantly changing. A single fixed estimate of return or volatility is often not enough for serious forecasting or risk analysis.

The long-term goal of this project is to build a system that can:

* model historical return behaviour
* estimate return and volatility
* simulate possible future market scenarios
* update forecasts using Bayesian logic
* generate risk-aware signals
* evaluate performance through backtesting

The current version focuses on the first stage: building a clean and runnable GBM baseline.

---

## Current Features

* Download historical market price data using `yfinance`
* Extract and process daily closing prices
* Calculate log returns from historical price data
* Estimate annualised drift and volatility
* Simulate future price paths using a GBM model
* Generate Monte Carlo price path simulations
* Save simulation plots to the `outputs/figures/` folder
* Run the full baseline pipeline from `main.py`

---

## Current Project Stage

This project is currently at the **GBM baseline foundation stage**.

Completed:

* data loading
* GBM parameter estimation
* Monte Carlo price path simulation
* plot generation
* runnable project pipeline

Planned future work:

* Bayesian updating layer
* posterior predictive forecasting
* trading or risk signal generation
* walk-forward backtesting
* comparison between GBM baseline and Bayesian forecasting results

---

## Project Structure

```text
Bayesian-Return-Forecasting-and-Backtesting-System/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── gbm_baseline.py
│   └── plotter.py
│
└── outputs/
    └── figures/
        └── gbm_paths.png
```

---

## Methodology

### 1. Data Loading

The project first loads historical market data for a selected ticker.

In the current version, the default ticker is:

```text
SPY
```

The data is downloaded using `yfinance`, and the adjusted closing price series is used for modelling.

---

### 2. Log Return Calculation

The price series is converted into log returns:

```text
log_return = log(P_t / P_{t-1})
```

Log returns are commonly used in quantitative finance because they are easier to work with mathematically and are suitable for continuous-time return modelling.

---

### 3. GBM Parameter Estimation

The GBM baseline estimates two key parameters:

```text
mu    = annualised drift
sigma = annualised volatility
```

The daily mean and standard deviation of log returns are estimated from historical data, then annualised using 252 trading days.

---

### 4. Monte Carlo Simulation

Using the estimated drift and volatility, the model simulates multiple possible future price paths.

The GBM model assumes that price evolves with both a deterministic trend and random market shocks.

The simulation currently generates:

```text
252 trading days
1000 simulated paths
```

---

### 5. Plot Output

The simulated paths are visualised and saved as:

```text
outputs/figures/gbm_paths.png
```

This provides a visual representation of possible future price movements under the GBM baseline model.

---


## Future Extensions

This project is planned to be extended in several directions.

### Bayesian Updating

Add a Bayesian model that updates prior beliefs about return and volatility using new market observations.

The core logic is:

```text
prior belief + new data = posterior updated belief
```

This will allow the model to produce updated forecasts as new data becomes available.

---

### Posterior Predictive Forecasting

Use posterior distributions to generate return forecasts with uncertainty ranges.

Instead of producing one fixed forecast, the model should estimate a distribution of possible future outcomes.

---

### Signal Generation

Convert forecasts into simple trading or risk signals.

Possible signals may include:

```text
risk-on
neutral
risk-off
```

or simple rules based on expected return and forecast uncertainty.

---

### Backtesting

Add a walk-forward backtesting module to test whether the forecasting signals would have worked historically.

The backtest should compare model-based signals against a simple benchmark such as buy-and-hold.

---

### Model Comparison

Compare the GBM baseline against the Bayesian forecasting model.

The goal is to evaluate whether Bayesian updating improves forecast usefulness compared with a fixed historical GBM estimate.

---

## Learning Goals

This project is designed to strengthen skills in:

* quantitative finance
* statistical modelling
* financial time-series analysis
* Monte Carlo simulation
* Bayesian forecasting
* Python project structure
* model evaluation and backtesting

---

## Disclaimer

This project is for educational and research purposes only. It is not financial advice and should not be used as a real trading or investment system without further validation, risk control, and professional review.
