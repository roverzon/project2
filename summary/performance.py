import pandas as pd
import pandas_ta as ta
from open_and_close.models import OpenClose
from datetime import timedelta


def custom_MACD(symbol, date):
    time_delta = 100
    trade = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=time_delta), date__lte=date).order_by('date')
    value = [[t.date,  t.open, t.high, t.low, t.close, t.volume] for t in trade]
    columns_name = ["date", "open", "high", "low", "close", "volume"]
    trade = pd.DataFrame(value, columns=columns_name).set_index("date")

    CustomMACDStrategy = ta.Strategy(
        name="EMAs, BBs, and MACD",
        description="Non Multiprocessing Strategy by rename Columns",
        ta=[
            {"kind": "macd", "fast": 8, "slow": 21},
            {"kind": "macd", "fast": 12, "slow": 26},
            {"kind": "macd", "fast": 14, "slow": 28},
        ]
    )
    trade.ta.strategy(CustomMACDStrategy)
    print(trade)


def custom_William(symbol, date):
    time_delta = 100
    trade = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=time_delta), date__lte=date).order_by('date')
    value = [[t.date,  t.open, t.high, t.low, t.close, t.volume] for t in trade]
    columns_name = ["date", "open", "high", "low", "close", "volume"]
    trade = pd.DataFrame(value, columns=columns_name).set_index("date")

    CustomMACDStrategy = ta.Strategy(
        name="EMAs, BBs, and MACD",
        description="Non Multiprocessing Strategy by rename Columns",
        ta=[
            {"kind": "macd", "fast": 8, "slow": 21},
            {"kind": "macd", "fast": 12, "slow": 26},
            {"kind": "macd", "fast": 14, "slow": 28},
        ]
    )
    trade.ta.strategy(CustomMACDStrategy)
    print(trade)
