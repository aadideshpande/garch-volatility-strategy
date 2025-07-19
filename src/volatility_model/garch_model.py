# src/volatility_model/garch_model.py

import pandas as pd
from arch import arch_model


def fit_garch_model(returns, p=1, q=1):
    """
    a function that accepts a returns time series, and 
    allows specifying the GARCH(p, q) order: 
    by default it uses GARCH(1,1), the most common version
    """
    returns = returns.dropna()

    # Fit a model where today’s volatility depends on
    # yesterday’s surprise and how volatile yesterday already was
    # using the MLE (Maximum Likelihood Estimation)
    model = arch_model(returns * 100, vol='Garch', p=p, q=q, mean='Zero', rescale=False)
    res = model.fit(disp='off')

    # give the std dev forecast for each time point in the historical data 
    fitted_vol = res.conditional_volatility / 100

    return res, fitted_vol
