import yfinance as yf


def get_us_indices_prices():
    sp500_data = yf.download("^GSPC", period="5d", progress=False)
    nasdaq_data = yf.download("^NDX", period="5d", progress=False)

    sp500_price = sp500_data["Close"].iloc[-1].item()
    nasdaq100_price = nasdaq_data["Close"].iloc[-1].item()

    messages = []
    messages.append(f"📈 标普500: {sp500_price:,.2f}")
    messages.append(f"📈 纳斯达克100: {nasdaq100_price:,.2f}")

    return messages
