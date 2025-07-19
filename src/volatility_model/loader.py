# src/volatility_model/loader.py

import yfinance as yf
import pandas as pd
import numpy as np
import warnings

def download_data(ticker='SPY', start='2005-01-01', end=None):
    df = yf.download(ticker, start=start, end=end, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(filter(None, col)).strip() for col in df.columns]

    # ✅ Rename adjusted close column for consistency
    if 'Close_SPY' in df.columns:
        df.rename(columns={'Close_SPY': 'price'}, inplace=True)
    elif 'Close' in df.columns:
        df.rename(columns={'Close': 'price'}, inplace=True)
    else:
        raise ValueError("Adjusted Close column not found in DataFrame.")

    # Compute log returns
    df['log_return'] = np.log(df['price'] / df['price'].shift(1))
    df.dropna(inplace=True)
    return df



def save_to_csv(df, path='data/spy_returns.csv'):
    df.to_csv(path)


def load_from_csv(path='data/spy_returns.csv'):
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    return df

if __name__ == "__main__":
    df_2 = download_data('SPY', start='2010-01-01')
    
    if df_2.empty:
        print("⚠️ WARNING: Data download failed — no file saved.")
    else:
        from pathlib import Path
        Path("data").mkdir(exist_ok=True)
        save_to_csv(df_2)
        print("✅ Data saved to data/spy_returns.csv")

