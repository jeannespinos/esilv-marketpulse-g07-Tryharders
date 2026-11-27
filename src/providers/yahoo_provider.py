import yfinance as yf


YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(canonical_ticker, period, interval):
    symbol = YAHOO_SYMBOLS[canonical_ticker]
    ticker = yf.Ticker(symbol)
    history = ticker.history(period=period, interval=interval, auto_adjust=False)

    if history.empty:
        raise ValueError("No Yahoo Finance data returned for " + symbol)

    rows = []
    for timestamp, line in history.iterrows():
        row = {}
        row["date"] = timestamp.strftime("%Y-%m-%d")
        row["ticker"] = canonical_ticker
        row["open"] = float(line["Open"])
        row["high"] = float(line["High"])
        row["low"] = float(line["Low"])
        row["close"] = float(line["Close"])
        row["volume"] = int(line["Volume"])
        rows.append(row)
    return rows