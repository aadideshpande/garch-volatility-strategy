# src/volatility_model/loader.py

import yfinance as yf
import pandas as pd
import numpy as np


def download_data(ticker='SPY', start='2005-01-01', end=None):
    """
    Downloads daily adjusted close prices for a given ticker.
    Returns a DataFrame with log returns.
    """
    df = yf.download(ticker, start=start, end=end)
    df.columns = [col[0] for col in df.columns]  # Keep only the first level: 'price'
    df = df[['Close']].rename(columns={'Close': 'price'})
    df.dropna(inplace=True)
    print(df.columns)
    print(df.index.name)
    print(df.head())
    df['log_return'] = np.log(df['price'] / df['price'].shift(1))

    # Mask out invalid values (e.g., price <= 0 or resulting log values being NaN or inf)
    df.loc[(df['price'] <= 0) | (df['price'].shift(1) <= 0), 'log_return'] = pd.NA
    df.dropna(inplace=True)
    return df


def save_to_csv(df, path='data/spy_returns.csv'):
    df.to_csv(path)


def load_from_csv(path='data/spy_returns.csv'):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df

# df = download_data('SPY', start='2010-01-01')
