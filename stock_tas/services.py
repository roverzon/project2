from open_and_close.models import OpenClose
from stock_tas.models import InvertedHammerRecord, BlackLineRecord, RedLineRecord, GapRecord, TrendingRecord
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import pandas_ta as ta
import pandas as pd
import numpy as np

time_delta = 50


def ticker_trade_pattern(symbol, date):
    tickers = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=time_delta), date__lte=date).order_by('-date')
    if len(tickers)-2 > 0:
        range_ = 0.68
        delta = 0.02
        diff_time_delta = 5.0
        gap_criteria = 0.06

        ticker_trade_0 = tickers[0]
        ticker_trade_1 = tickers[1]
        close_ = [t.close for t in tickers]

        gap = ticker_trade_0.open - ticker_trade_1.close
        is_gap = True if abs(gap/ticker_trade_0.open) > gap_criteria else False

        ticker_close_ordered = sorted(close_)
        ticker_close_ordered_reverse = sorted(close_, reverse=True)

        close_index = ticker_close_ordered.index(ticker_trade_0.close)
        close_index_reversed = ticker_close_ordered_reverse.index(ticker_trade_0.close)

        ticker_volume_ordered = sorted([t.volume for t in tickers])
        volume_index = ticker_volume_ordered.index(ticker_trade_0.volume)

        price_lift = ticker_trade_0.close/ticker_trade_1.close
        volume_lift = ticker_trade_0.volume/ticker_trade_1.volume

        close_and_open_diff = ticker_trade_0.close - ticker_trade_0.open
        close_and_open_lift = close_and_open_diff / ticker_trade_0.open
        true_range = ticker_trade_0.high - ticker_trade_0.low

        diff_times = abs(true_range) / abs(close_and_open_diff) if close_and_open_diff != 0.0 else 0.0

        if close_and_open_diff > 0:
            is_lift = True
        else:
            is_lift = False

        if abs(close_and_open_lift) > 0.15:
            line_type = 'L'
        else:
            line_type = 'M'

        if len(ticker_volume_ordered) - volume_index < 3:
            is_high_exchange = True
        else:
            is_high_exchange = False

        if len(ticker_close_ordered) - close_index < 3:
            is_upper = True
        else:
            is_upper = False

        if len(ticker_close_ordered_reverse) - close_index_reversed < 3:
            is_down = True
        else:
            is_down = False

        if abs(close_and_open_diff)/abs(true_range) > range_:

            if close_and_open_diff < 0.0:
                br = BlackLineRecord(
                    date=date,
                    symbol=symbol,
                    line_type=line_type,
                    close=ticker_trade_0.close,
                    price_lift=round(price_lift, 5),
                    is_upper=is_upper,
                    is_down=is_down,
                    true_range=true_range,
                    volume=ticker_trade_0.volume,
                    volume_lift=round(volume_lift, 5),
                    is_high_exchange=is_high_exchange,
                    range_threshold=range_
                )

                try:
                    br.save()
                    print(f'Black_Line - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                except:
                    pass
            else:

                red_line = RedLineRecord(
                    date=date,
                    symbol=symbol,
                    line_type=line_type,
                    close=ticker_trade_0.close,
                    price_lift=round(price_lift, 5),
                    is_upper=is_upper,
                    is_down=is_down,
                    true_range=true_range,
                    volume=ticker_trade_0.volume,
                    volume_lift=round(volume_lift, 5),
                    is_high_exchange=is_high_exchange,
                    range_threshold=range_
                )

                try:
                    red_line.save()
                    print(f'Red_Line - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                except:
                    pass

        if diff_times > diff_time_delta and close_and_open_lift < delta:
            record= InvertedHammerRecord(
                date=date,
                symbol=symbol,
                is_lift=is_lift,
                lift=round(close_and_open_lift, 5),
                volume=ticker_trade_0.volume,
                volume_lift=round(volume_lift, 5),
                is_high_exchange=is_high_exchange,
                is_upper=is_upper,
                is_down=is_down,
                close=ticker_trade_0.close,
                delta=delta,
                diff_time_delta=diff_time_delta,
            )

            try:
                print(f'INVERTED_HAMMER - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                record.save()
            except:
                pass

        if is_gap:
            is_upper_gap = True if gap > 0 else False
            gap = GapRecord(
                date=date,
                symbol=symbol,
                price_lift=round(gap, 5),
                range_threshold=gap_criteria,
                is_upper=is_upper_gap
            )

            try:
                print(f'GAP - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                gap.save()
            except:
                pass


def cross_star_api(symbol, from_, end_):
    dates = pd.bdate_range(start=from_, end=end_)
    for date in dates:
        ticker_trade_pattern(symbol=symbol, date=date)


def stock_linear_trending_api(symbol, date):
    time_delta = 50
    tickers = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=time_delta), date__lte=date).order_by('-date')
    close = pd.DataFrame([[t.date, t.close, t.volume ] for t in tickers], columns=["date", "close", "volume"]).set_index("date")
    print(tickers)

    if 5 < len(tickers) < 10:
        CustomMACDStrategy = ta.Strategy(
            name="EMAs, BBs, and MACD",
            description="Non Multiprocessing Strategy by rename Columns",
            ta=[
                {"kind": "sma", "length": 5},
            ]
        )
        close.ta.strategy(CustomMACDStrategy)

        trend = TrendingRecord(
            date=date,
            symbol=symbol,
            close=tickers[0].close,
            sma_5d=close['SMA_5'][-1],
            cross_sma5=tickers[0].close - close['SMA_5'][-1],
        )

        trend.save()

    if 10 <= len(tickers) < 20:
        CustomMACDStrategy = ta.Strategy(
            name="EMAs, BBs, and MACD",
            description="Non Multiprocessing Strategy by rename Columns",
            ta=[
                {"kind": "sma", "length": 5},
                {"kind": "sma", "length": 10},
            ]
        )
        close.ta.strategy(CustomMACDStrategy)

        trend = TrendingRecord(
            date=date,
            symbol=symbol,
            close=tickers[0].close,
            sma_5d=close['SMA_5'][-1],
            sma_10d=close['SMA_10'][-1],
            cross_sma5=tickers[0].close - close['SMA_5'][-1],
            cross_sma10=tickers[0].close - close['SMA_10'][-1],
        )

        trend.save()

    if 20 <= len(tickers) < 30:
        CustomMACDStrategy = ta.Strategy(
            name="EMAs, BBs, and MACD",
            description="Non Multiprocessing Strategy by rename Columns",
            ta=[
                {"kind": "sma", "length": 5},
                {"kind": "sma", "length": 10},
                {"kind": "sma", "length": 20},
            ]
        )
        close.ta.strategy(CustomMACDStrategy)

        X = np.array([i for i in range(len(tickers[:20]))]).reshape((-1, 1))
        y = np.array([t.close for t in tickers[:20]])
        model = LinearRegression()
        reg = model.fit(X=X, y=y)
        slope = round(reg.coef_, 5)
        angle = round(np.rad2deg(np.arctan2(y[-1] - y[0], X[-1] - X[0])), 5)

        trend = TrendingRecord(
            date=date,
            symbol=symbol,
            close=tickers[0].close,
            sma_5d=close['SMA_5'][-1],
            sma_10d=close['SMA_10'][-1],
            sma_20d=close['SMA_20'][-1],
            cross_sma5=tickers[0].close - close['SMA_5'][-1],
            cross_sma10=tickers[0].close - close['SMA_10'][-1],
            cross_sma20=tickers[0].close - close['SMA_20'][-1],
            angle=angle,
            slope=slope
        )

        trend.save()

    if 30 <= len(tickers):
        CustomMACDStrategy = ta.Strategy(
            name="EMAs, BBs, and MACD",
            description="Non Multiprocessing Strategy by rename Columns",
            ta=[
                {"kind": "sma", "length": 5},
                {"kind": "sma", "length": 10},
                {"kind": "sma", "length": 20},
                {"kind": "sma", "length": 30},
            ]
        )

        close.ta.strategy(CustomMACDStrategy)
        X = np.array([i for i in range(len(tickers[:20]))]).reshape((-1, 1))
        y = np.array([t.close for t in tickers[:20]])
        model = LinearRegression()
        reg = model.fit(X=X, y=y)
        slope = round(reg.coef_, 5)
        angle = round(np.rad2deg(np.arctan2(y[-1] - y[0], X[-1] - X[0])), 5)

        trend = TrendingRecord(
            date=date,
            symbol=symbol,
            close=tickers[0].close,
            sma_5d=close['SMA_5'][-1],
            sma_10d=close['SMA_10'][-1],
            sma_20d=close['SMA_20'][-1],
            sma_30d=close['SMA_30'][-1],
            cross_sma5=tickers[0].close - close['SMA_5'][-1],
            cross_sma10=tickers[0].close - close['SMA_10'][-1],
            cross_sma20=tickers[0].close - close['SMA_20'][-1],
            cross_sma30=tickers[0].close - close['SMA_30'][-1],
            angle=angle,
            slope=slope
        )

        trend.save()

