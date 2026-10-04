import yfinance as yf
import analysis.scoring as sc

TICKERS = ["AAON", "SNDK", "MU", "NVDA", "TSM", "CRWV",
           "AAPL", "MSFT", "GOOGL", "META", "AMZN", "ASML"
           ,"AMD", "INTC", "AVGO", "CEG", "NEE", "TSLA",
           "VST", "ETN", "SPCX","META"]

results = []
for ticker in TICKERS:
    score = sc.run_scoring(ticker)
    results.append({
        "ticker": ticker,
        "total": score["total"],
        "recommendation": score["recommendation"],
        "analyst": score["analyst"]
    })

results.sort(key=lambda x: x["total"], reverse=True)

print(f"\n{'Ticker':<8} {'Total':<8} {'Signal':<8} {'Analytiker'}")
print("-" * 40)
for r in results:
    print(f"{r['ticker']:<8} {r['total']:<8.1f} {r['recommendation']:<8} {r['analyst']}")

    





