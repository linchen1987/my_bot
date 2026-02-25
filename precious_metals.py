import yfinance as yf


def get_precious_metals_prices():
    gold = yf.Ticker("GC=F")
    silver = yf.Ticker("SI=F")

    gold_price = gold.history(period="1d")["Close"].iloc[-1]
    silver_price = silver.history(period="1d")["Close"].iloc[-1]

    oz_to_g = 28.3495
    gold_price_g = gold_price / oz_to_g
    silver_price_g = silver_price / oz_to_g

    messages = []
    messages.append(f"🥇 黄金: ${gold_price_g:,.2f}/克")
    messages.append(f"🥈 白银: ${silver_price_g:,.2f}/克")

    return messages
