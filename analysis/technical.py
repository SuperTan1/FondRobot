import yfinance as yf

def get_technical_data(ticker) -> dict:
    stock = yf.Ticker(ticker)
    hist = stock.history("1y")

    change = hist["Close"].diff().dropna()

    winMedel = change.clip(lower = 0).rolling(14).mean()
    loseMedel = change.clip(upper = 0).rolling(14).mean()

    RS = winMedel/(loseMedel * -1)
    RSI = 100 - (100/ (1 + RS)).iloc[-1]

    SMA50 = hist["Close"].rolling(50).mean().iloc[-1]
    SMA200 = hist["Close"].rolling(200).mean().iloc[-1]

    EMA12 = hist["Close"].ewm(span=12).mean()
    EMA26 = hist["Close"].ewm(span=26).mean()
    MACD = EMA12 - EMA26
    MACDLastLine = MACD.iloc[-1]
    signal = MACD.ewm(span=9).mean()
    signalLastLine = signal.iloc[-1]

    middleLine = hist["Close"].rolling(20).mean()
    overLine = (middleLine + 2*hist["Close"].rolling(20).std()).iloc[-1]
    lowerLine = (middleLine - 2*hist["Close"].rolling(20).std()).iloc[-1]
    
    tPrice = hist["Close"].iloc[-1]

    return {
        "Today price ": tPrice,
        "SMA50 ": SMA50,
        "SMA200 ": SMA200,
        "MACD ": MACDLastLine,
        "Signal ": signalLastLine,
        "OverLine ": overLine,
        "LowerLine ": lowerLine,
        "RSI ": RSI
    }

if __name__ == "__main__":
    for key, value in get_technical_data("AAON").items():
        print(f"{key}: {value}")

