# src/volatility_model/strategy.py

import pandas as pd
import numpy as np

def classify_volatility_regimes(df, vol_col='garch_vol', threshold_quantile=0.7):
    """
    Classify each day into high or low volatility regimes based on a quantile threshold.
    Adds a column 'vol_regime' with values: 'low' or 'high'.
    """
    threshold = df[vol_col].quantile(threshold_quantile)
    df['vol_regime'] = df[vol_col].apply(lambda x: 'high' if x > threshold else 'low')
    return df

def compute_performance_metrics(df, return_col, risk_free_rate=0.0, periods_per_year=252):
    """
    Computes Sharpe ratio, volatility, and max drawdown for given return series.
    Returns a dictionary of metrics.
    """
    returns = df[return_col].dropna()

    vol = returns.std() * np.sqrt(periods_per_year)
    
    total_return = np.exp(returns.sum())
    num_years = (df.index[-1] - df.index[0]).days / 365.25
    cagr = total_return**(1/num_years) - 1
    
    sharpe = ((returns.mean() - risk_free_rate) / returns.std()) * np.sqrt(periods_per_year)

    wealth_index = returns.cumsum().apply(np.exp)
    peak = wealth_index.cummax()
    drawdown = (wealth_index - peak) / peak
    max_dd = drawdown.min()

    return {
        'CAGR': cagr,
        'Volatility': vol,
        'Sharpe Ratio': sharpe,
        'Max Drawdown': max_dd
    }
