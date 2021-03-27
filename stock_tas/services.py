from open_and_close.models import OpenClose
from stock_tas.models import CrossStarRecord
from datetime import datetime, timedelta


def cross_star(symbol, date):
    tickers = OpenClose.objects.filter(symbol=symbol, date__gte=date-timedelta(days=5), date__lte=date)
    volume_lift = 0.0
    if len(tickers)-1>0:
        ticker_trade = tickers[len(tickers)-1]
        ticker_trade_1 = tickers[len(tickers)-2]
        volume_lift = ticker_trade.volume/ticker_trade_1.volume

        close_and_open_diff = ticker_trade.close - ticker_trade.open
        close_and_open_lift = close_and_open_diff / ticker_trade.open
        high_and_low_lift_diff = ticker_trade.high - ticker_trade.low

        delta = 0.02
        diff_time_delta = 10

        diff_times = abs(high_and_low_lift_diff) / abs(close_and_open_diff) if close_and_open_diff != 0.0 else 0.0
        is_star = False

        if diff_times > diff_time_delta and close_and_open_lift < delta:
            is_star = True
            if close_and_open_diff > 0:
                is_lift = True
            else:
                is_lift = False

            if volume_lift > 2.0:
                is_high_lift = True
            else:
                is_high_lift = False

            record= CrossStarRecord(
                date=date,
                symbol=symbol,
                is_star=is_star,
                is_lift=is_lift,
                lift=round(close_and_open_lift, 5),
                volume=ticker_trade.volume,
                volume_lift=round(volume_lift, 5),
                is_high_lift=is_high_lift,
                close=ticker_trade.close,
                delta=delta,
                diff_time_delta=diff_time_delta,
            )

            try:
                print(f'Ticker:{symbol} on Date: {date} '.format(symbol=symbol, date=date))
                record.save()
            except:
                pass
        return is_star
