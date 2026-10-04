import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_news_count(ticker):
    stock = yf.Ticker(ticker)
    stock_news = stock.news
    analyzer = SentimentIntensityAnalyzer()
    titleScore = 0

    for item in stock_news:
        title = analyzer.polarity_scores(item["content"]["title"])["compound"]
        titleScore += title

    compund = titleScore/len(stock_news)

    return compund

if __name__ == "__main__":
    print(get_news_count("AAON"))

