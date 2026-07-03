import yfinance as yf
import pandas as pd


TICKERS = ["AAPL", "MSFT", "GOOGL", "NVDA", "META"]

def fetch_prices(tickers: list[str], period: str) -> pd.DataFrame:
    data = yf.download(tickers, period=period)
    return data

def fetch_latest_prices(tickers: list[str]):
    data = fetch_prices(tickers, "5d")
    latest_data = data.iloc[-1]
    return latest_data








