import yfinance as yf
import pandas as pd
from pathlib import Path
import time

def catch_file(path, max_time=86400):
    p = Path(path)
    if p.exists():
        latest_save = p.stat().st_mtime
        current_time = time.time()
        under_aday = current_time - latest_save
        if(under_aday<max_time):
            file = pd.read_parquet(path)
            return file

def fetch_history(ticker, period="10y") -> pd.DataFrame:
    tickerN = ticker.replace("^","")
    path = Path("cache") / f"{tickerN}.parquet"
    catched = catch_file(path)
    if catched is None:
        df = yf.Ticker(ticker).history(period=period, auto_adjust=True)
        Path("cache").mkdir(exist_ok=True)
        df = df[["Open", "High", "Low", "Close", "Volume"]]
        df = df.dropna()
        df.index = df.index.tz_localize(None)
        df.index = df.index.normalize()
        df.to_parquet(path)
        return df
    return catched

def fetch_market() -> pd.DataFrame:
    sp500 = fetch_history("^GSPC")["Close"]
    vix = fetch_history("^VIX")["Close"]
    df = pd.concat([sp500,vix], axis=1)
    df.columns = ["sp500","vix"]
    return df





if __name__ == "__main__":
   print(fetch_history("AAPL"))
   market = fetch_market()
   print(market.tail())
   print(market.shape)
    





