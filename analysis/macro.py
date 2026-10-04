import yfinance as yf

def get_macro_data() -> dict:
    spFunds = yf.Ticker("^GSPC")
    spHistory = spFunds.history(period ="1mo")
    close = spHistory["Close"].dropna()
    spFirstDay = close.iloc[0]
    spLastDay = close.iloc[-1]
    spMonthlyChange = (spLastDay / spFirstDay - 1) * 100

    fiveCloseDay = yf.Ticker("^VIX").history(period = "5d")
    VIX = fiveCloseDay["Close"].iloc[-1]

    tenYearInterest = yf.Ticker("^TNX").history(period="5d")["Close"].iloc[-1]

    XLIClosing = yf.Ticker("XLI").history(period="1mo")["Close"].dropna()
    xliFirst = XLIClosing.iloc[0]
    xliLast = XLIClosing.iloc[-1]
    XLI = (xliLast / xliFirst -1 ) * 100
    
    
    return {
        "sp500 monthly percentage change ": spMonthlyChange,
        "VIX is ": VIX,
        "tenYearInterest is ": tenYearInterest,
        "XLI is ": XLI
    }


if __name__ == "__main__":
    for key, value in get_macro_data().items():
        print(f"{key} {value}")
    