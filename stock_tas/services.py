from open_and_close.models import OpenClose
from stock_tas.models import InvertedHammer, BlackLineRecord
from datetime import datetime, timedelta
import pandas as pd


def black_line(symbol, date):
    tickers = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=5), date__lte=date).order_by('-date')
    if len(tickers)-2>0:
        ticker_trade = tickers[0]
        ticker_trade_1 = tickers[1]
        volume_lift = ticker_trade.volume/ticker_trade_1.volume

        close_and_open_diff = ticker_trade.close - ticker_trade.open
        close_and_open_lift = close_and_open_diff / ticker_trade.open
        true_range = ticker_trade.high - ticker_trade.low
        range_ = 0.68

        if close_and_open_diff/abs(true_range) > range_:
            if abs(close_and_open_lift) > 0.15:
                line_type = 'L'
            else:
                line_type ='M'

            if volume_lift > 2.0:
                is_high_exchange = True
            else:
                is_high_exchange = False

            br = BlackLineRecord(
                date=date,
                symbol=symbol,
                line_type=line_type,
                close=ticker_trade.close,
                true_range=true_range,
                volume=ticker_trade.volume,
                volume_lift=round(volume_lift, 5),
                is_high_exchange=is_high_exchange,
                range_threshold=range_
            )

            br.save()
            print(f'Black_Line - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))


def label_inverted_hammer_pattern(symbol, date):
    tickers = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=10), date__lte=date).order_by('-date')
    ticker_close_ordered = sorted([t.close for t in tickers])
    ticker_close_ordered_reverse = sorted([t.close for t in tickers], reverse=True)
    is_star = False
    if len(tickers)-2>0:
        ticker_trade = tickers[0]
        ticker_trade_1 = tickers[1]
        volume_lift = ticker_trade.volume/ticker_trade_1.volume

        close_index = ticker_close_ordered.index(ticker_trade.close)
        close_index_reversed = ticker_close_ordered_reverse.index(ticker_trade.close)

        close_and_open_diff = ticker_trade.close - ticker_trade.open
        close_and_open_lift = close_and_open_diff / ticker_trade.open
        true_range = ticker_trade.high - ticker_trade.low

        delta = 0.02
        diff_time_delta = 10.0

        diff_times = abs(true_range) / abs(close_and_open_diff) if close_and_open_diff != 0.0 else 0.0

        if diff_times > diff_time_delta and close_and_open_lift < delta:
            if close_and_open_diff > 0:
                is_lift = True
            else:
                is_lift = False

            if volume_lift > 2.0:
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

            record= InvertedHammer(
                date=date,
                symbol=symbol,
                is_lift=is_lift,
                lift=round(close_and_open_lift, 5),
                volume=ticker_trade.volume,
                volume_lift=round(volume_lift, 5),
                is_high_exchange=is_high_exchange,
                is_upper=is_upper,
                is_down=is_down,
                close=ticker_trade.close,
                delta=delta,
                diff_time_delta=diff_time_delta,
            )
            is_star=True

            try:
                print(f'INVERTED_HAMMER - Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                record.save()
            except:
                pass
        return is_star


def cross_star_api(symbol, from_, end_):
    dates = pd.bdate_range(start=from_, end=end_)
    for date in dates:
        label_inverted_hammer_pattern(symbol=symbol, date=date)
