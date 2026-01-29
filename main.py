import os
import requests
from dotenv import load_dotenv

from crypto import get_crypto_price
from a_stock import get_a_stock_prices

load_dotenv()


def main():
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("请在 .env 文件中设置 TELEGRAM_BOT_TOKEN 和 TELEGRAM_CHAT_ID")

    messages = []
    messages.extend(get_crypto_price())
    messages.extend(get_a_stock_prices())

    message = "\n".join(messages)

    send_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
    requests.get(send_url)


if __name__ == "__main__":
    main()
