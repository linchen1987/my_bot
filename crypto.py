import requests


def format_price(price):
    if price >= 1:
        return f"{price:,.2f}"

    price_str = f"{price:.10f}".rstrip("0").rstrip(".")
    decimal_part = price_str.split(".")[1]

    leading_zeros = len(decimal_part) - len(decimal_part.lstrip("0"))
    decimals_needed = min(leading_zeros + 2, 7)

    return f"{price:.{decimals_needed}f}"


def get_crypto_price():
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,flare-networks,arcblock,solana&vs_currencies=usd"
    response = requests.get(api_url).json()

    messages = []
    messages.append(f"💰 BTC: ${format_price(response['bitcoin']['usd'])} USD")
    messages.append(f"💰 ETH: ${format_price(response['ethereum']['usd'])} USD")
    messages.append(f"💰 FLR: ${format_price(response['flare-networks']['usd'])} USD")
    messages.append(f"💰 ABT: ${format_price(response['arcblock']['usd'])} USD")
    messages.append(f"💰 SOL: ${format_price(response['solana']['usd'])} USD")

    return messages
