import os
import requests
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("请在 .env 文件中设置 BOT_TOKEN 和 CHAT_ID")

    # 1. 获取价格
    api_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(api_url).json()
    price = response["bitcoin"]["usd"]

    # 2. 准备发送消息
    bot_token = BOT_TOKEN
    chat_id = CHAT_ID # (注意，频道ID可能是 @channel_name 或一个负数)
    message = f"BTC 每日价格: ${price:,} USD"

    # 3. 通过 Telegram Bot API 发送
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_url)


if __name__ == "__main__":
    main()
