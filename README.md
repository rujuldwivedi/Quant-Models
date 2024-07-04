# Quant Models

This repository contains implementations of various quantitative finance models. It includes Jupyter notebooks (`.ipynb` files) for three main models: Black-Scholes, Fourier Transform, Kalman Filter, and Option Pricing. Additionally, it has configuration files in YAML and TOML formats for model information and two subfolders: `src` for C and FMNM (Financial Model Numerical Methods) implementations, and `data` for hosting historical and Google data.

## Overview

Quant Models is a collection of quantitative finance models implemented in Jupyter notebooks, with additional C and FMNM implementations. It includes models for option pricing, time series analysis, and more.

## Quantitative Models

### Black-Scholes Model

The Black-Scholes model is a mathematical model for pricing an options contract. It calculates the price of a European call or put option based on factors such as the underlying asset price, strike price, volatility, time to expiration, and the risk-free rate.

### Fourier Transform

The Fourier Transform model is used to transform time-domain data into frequency-domain data. It's widely used in signal processing and can also be applied in finance for analyzing time series data.

### Kalman Filter

The Kalman Filter is an algorithm that uses a series of measurements observed over time, containing statistical noise and other inaccuracies, and produces estimates of unknown variables. It's used in finance for tracking and predicting time series data.

### Option Pricing

This model includes various methods for option pricing beyond Black-Scholes, using different numerical techniques and simulations.

## Acknowledgements
The Black-Scholes model implementation is inspired by the classic model introduced by Fischer Black and Myron Scholes.
Fourier Transform methods are based on standard mathematical transformations used in signal processing.
Kalman Filter algorithms follow the original work of Rudolf E. Kálmán.
Option pricing techniques are adapted from various financial literature.
Feel free to reach out if you have any questions or suggestions!

Happy coding!
