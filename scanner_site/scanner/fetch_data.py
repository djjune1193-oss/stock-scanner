import pandas as pd
import time
from datetime import datetime, timedelta
import yfinance as yf

def get_historical_stock_data(ticker_symbol, start_date=None, end_date=None, interval="1d"):
    
    today = pd.Timestamp.today().date()
    lookback_days=365
    
    if start_date is None:
        start_date = start_date = today - timedelta(days=lookback_days)
    if end_date is None:
        end_date = end_date = today + timedelta(days=1)

    ticker = yf.Ticker(ticker_symbol)

    try:
        # Fetch data
        df = ticker.history(start=start_date, end=end_date, interval=interval)

        if df.empty:
            print(f"No data found for {ticker_symbol} within the specified date range and interval.")
            return None
        else:
            return df

    except Exception as e:
        print(f"An error occurred while fetching data for {ticker_symbol}: {e}")
        return None
