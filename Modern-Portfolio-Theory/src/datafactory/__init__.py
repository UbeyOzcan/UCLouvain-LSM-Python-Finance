import pandas as pd
import yfinance as yf
import numpy as np

def get_closing(ticker:list, start_dt:str=None, end_dt:str=None) -> pd.DataFrame:
    return yf.download(tickers=ticker, start=start_dt, end=end_dt)['Close']

def stock_return(prices:pd.DataFrame) -> pd.DataFrame:
    return np.log(prices / prices.shift(1))