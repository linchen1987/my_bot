import requests


def get_crypto_price():
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,flare-networks,arcblock,solana&vs_currencies=usd"
    response = requests.get(api_url).json()

    messages = []
    messages.append(f"💰 BTC: ${response['bitcoin']['usd']:,.2f} USD")
    messages.append(f"💰 ETH: ${response['ethereum']['usd']:,.2f} USD")
    messages.append(f"💰 FLR: ${response['flare-networks']['usd']:,.2f} USD")
    messages.append(f"💰 ABT: ${response['arcblock']['usd']:,.2f} USD")
    messages.append(f"💰 SOL: ${response['solana']['usd']:,.2f} USD")

    return messages
