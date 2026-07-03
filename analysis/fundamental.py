import yfinance as yf

def get_fundamental_data(ticker: str):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        # Företagsinfo
        "Company":              info.get("longName"),
        "Sector":               info.get("sector"),
        "Industry":             info.get("industry"),

        # Värdering
        "Market Cap":           info.get("marketCap"),
        "P/E Ratio":            info.get("trailingPE"),
        "Forward P/E":          info.get("forwardPE"),
        "P/B Ratio":            info.get("priceToBook"),
        "EV/EBITDA":            info.get("enterpriseToEbitda"),

        # Vinst & tillväxt
        "EPS":                  info.get("trailingEps"),
        "Earnings Growth":      info.get("earningsGrowth"),
        "Revenue Growth":       info.get("revenueGrowth"),
        "Profit Margin":        info.get("profitMargins"),

        # Finansiell hälsa
        "Debt to Equity":       info.get("debtToEquity"),
        "Current Ratio":        info.get("currentRatio"),
        "Return on Equity":     info.get("returnOnEquity"),
        "Return on Assets":     info.get("returnOnAssets"),
        "Free Cash Flow":       info.get("freeCashflow"),

        # Aktieinfo
        "Current Price":        info.get("currentPrice"),
        "52W High":             info.get("fiftyTwoWeekHigh"),
        "52W Low":              info.get("fiftyTwoWeekLow"),
        "Dividend Yield":       info.get("dividendYield"),
        "Beta":                 info.get("beta"),

        # Analytiker
        "Target Price":         info.get("targetMeanPrice"),
        "Recommendation":       info.get("recommendationKey"),
    }

if __name__ == "__main__":
    data = get_fundamental_data("AAPL")
    for key, value in data.items():
        print(f"{key}: {value}")

