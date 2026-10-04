from analysis.technical import get_technical_data
from analysis.macro import get_macro_data
from analysis.fundamental import get_fundamental_data 
from analysis.sentiment import get_news_count

def get_technical_scoring(ticker): 
    score = 0
    technical_data = get_technical_data(ticker)
    RSI = technical_data["RSI "]
    if(RSI < 30):
        score += 25
    elif(30 < RSI < 40):
        score += 10
    elif(40 <= RSI <= 60):
        score += 0
    elif(60 < RSI < 70):
        score -= 10
    else:
        score -= 25
    
    SMA50 = technical_data["SMA50 "]
    SMA200 = technical_data["SMA200 "]
    tPrice = technical_data["Today price "]

    if(tPrice > SMA50 and tPrice > SMA200):
        score +=20
    elif(tPrice > SMA200 and tPrice < SMA50):
        score += 10
    elif(tPrice < SMA50 and tPrice < SMA200):
        score -= 20
    
    MACD = technical_data["MACD "]
    Signal = technical_data["Signal "]

    if(MACD > Signal):
        score += 20
    else: 
        score -= 20
    
    OverLine = technical_data["OverLine "]
    LowerLine = technical_data["LowerLine "]

    if((tPrice - LowerLine) / LowerLine < 0.05):
        score += 15
    
    if((OverLine - tPrice) / OverLine < 0.05):
        score -= 15

    return score 


def get_fundamental_scoring(ticker):
    fundamental_data = get_fundamental_data(ticker)
    EaringsGrowth = fundamental_data["Earnings Growth"] or 0
    RevenueGrowth = fundamental_data["Revenue Growth"] or 0
    PE = fundamental_data["P/E Ratio"] or 0
    CurrentRatio = fundamental_data["Current Ratio"] or 0
    DebtEquity = fundamental_data["Debt to Equity"] or 0
    score = 0

    if(EaringsGrowth > 0.2):
        score += 25
    elif(EaringsGrowth > 0):
        score += 10
    else:
        score -= 25
    
    if(RevenueGrowth > 0.15):
        score += 20
    elif(RevenueGrowth > 0):
        score += 10
    else: 
        score -=15
    
    if(PE < 15):
        score +=20
    elif(PE > 15 and PE < 25):
        score += 10
    elif(PE > 40):
        score -= 20
    
    if(CurrentRatio > 2):
        score +=15
    else: 
        score -= 20
    
    if(DebtEquity > 2):
        score -= 25

    return score


def get_macro_scoring():
    macro_data = get_macro_data()
    SP500 = macro_data["sp500 monthly percentage change "]
    VIX = macro_data["VIX is "]
    Interest = macro_data["tenYearInterest is "]
    XLI = macro_data["XLI is "]
    score = 0

    if (SP500 > 0.02):
        score += 20
    elif (SP500 > 0):
        score += 10
    else: 
        score -= 20
    
    if(VIX < 15):
        score +=20
    elif (15 < VIX and VIX < 20):
        score += 10
    elif (20 < VIX and VIX < 30):
        score += -10
    else: 
        score -= 25

    if(Interest < 3):
        score += 15
    elif (3 < Interest and Interest < 4):
        score += 5
    elif (4 < Interest and Interest < 5):
        score -= 10
    else:
        score -= 20

    if (XLI > 0.02):
        score += 15
    elif (XLI > 0):
        score += 5
    else:
        score -= 15

    return score

def get_sentiment_scoring(ticker):
    data_sentiment = get_news_count(ticker)
    score = 0
    if(data_sentiment > 0.2):
        score += 25
    elif(data_sentiment > 0.05):
        score += 10
    elif(-0.05 < data_sentiment and data_sentiment < 0.05):
        score += 0
    elif(data_sentiment < -0.05):
        score -= 10
    elif(data_sentiment < -0.2):
        score -= 25
    
    return score
    
def run_scoring(ticker):
    technical = get_technical_scoring(ticker)
    fundamental = get_fundamental_scoring(ticker)
    macro = get_macro_scoring()
    sentiment = get_sentiment_scoring(ticker)
    analyst = get_fundamental_data(ticker).get("Recommendation") or "N/A"

    total = ((technical * 0.4) + (fundamental * 0.4)
            + (macro * 0.1) + (sentiment * 0.1))

    if total > 20:
        recommendation = "KÖP"
    elif total > -30:
        recommendation = "HÅLL"
    else:
        recommendation = "SÄLJ"

    return {
        "total": total,
        "technical": technical,
        "fundamental": fundamental,
        "macro": macro,
        "sentiment": sentiment,
        "recommendation": recommendation,
        "analyst": analyst
    }


if __name__ == "__main__":
    ticker = "MU"
    score = run_scoring(ticker)

    print(f"\n=== {ticker} ===")
    print(f"Teknisk:     {score['technical']}")
    print(f"Fundamental: {score['fundamental']}")
    print(f"Makro:       {score['macro']}")
    print(f"Sentiment:   {score['sentiment']}")
    print(f"Total:       {score['total']:.1f}")
    print(f"Signal:      {score['recommendation']}")
    print(f"Analytiker:  {score['analyst']}\n")

    print("--- Teknisk ---")
    for key, value in get_technical_data(ticker).items():
        print(f"{key}: {value}")

    print("\n--- Fundamental ---")
    for key, value in get_fundamental_data(ticker).items():
        print(f"{key}: {value}")
