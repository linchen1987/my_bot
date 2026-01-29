import akshare as ak


def get_a_stock_price(index_code, index_name):
    df = ak.stock_zh_index_spot_sina()
    df_filtered = df[df["代码"] == index_code]

    if not df_filtered.empty:
        row = df_filtered.iloc[0]
        close = row["最新价"]
        change = row["涨跌幅"]
        return f"📊 {index_name}: {close} ({change}%)"
    else:
        return f"📊 {index_name}: 无数据"


def get_a_stock_prices():
    index_list = [
        ("sh000001", "上证指数"),
        # ("sz399001", "深证成指"),
        # ("sz399006", "创业板指"),
        ("sh000300", "沪深300"),
    ]
    messages = []
    for index_code, index_name in index_list:
        messages.append(get_a_stock_price(index_code, index_name))
    return messages
