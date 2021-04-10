from stock_tas.models import RedLineRecord, InvertedHammerRecord, BlackLineRecord
from tickers.models import Ticker
from tickers.banchmark_list import get_white_list
from datetime import datetime, timedelta
from open_and_close.models import OpenClose
from summary.models import TickerReturn, TickerPerformancePercentile
from scipy import stats
import numpy as np
import pandas as pd


def candle_chart_technical_api(date):
    rl_ticker_list = [t.symbol for t in RedLineRecord.objects.filter(date__exact=date)]
    bl_ticker_list = [t.symbol for t in BlackLineRecord.objects.filter(date__exact=date)]
    ibr_ticker_list = [t.symbol for t in InvertedHammerRecord.objects.filter(date__exact=date)]

    summary = [
        {
            "name": "inverted_hammer",
            "tickers": ibr_ticker_list
        },
        {
            "name": "red_line",
            "tickers": rl_ticker_list
        },
        {
            "name": "black_line",
            "tickers": bl_ticker_list
        }
    ]

    return summary


def ticker_price_return_api(is_sampled=True):
    today = datetime.now()
    if is_sampled:
        symbols = [t.symbol for t in Ticker.objects.all() if t.symbol in get_white_list()['symbols']]
    else:
        symbols = [t.symbol for t in Ticker.objects.all()]

    for symbol in symbols:
        trades = OpenClose.objects.filter(symbol=symbol, date__gte=today-timedelta(days=300), date__lte=today).order_by('-date')
        return_on_price = []
        for frame in [7, 14, 30, 60, 90, 180]:
            try:
                trade_price_1d = trades[0].close
                return_on_price.append(round(trade_price_1d/trades[frame-1].close, 5)-1.0)
            except:
                return_on_price.append(np.nan)

        price_return = TickerReturn(
            date=today.strftime('%Y-%m-%d'),
            symbol=symbol,
            price_return_7d=return_on_price[0],
            price_return_14d=return_on_price[1],
            price_return_30d=return_on_price[2],
            price_return_60d=return_on_price[3],
            price_return_90d=return_on_price[4],
            price_return_180d=return_on_price[5],
        )

        try:
            price_return.save()
            print(f"Symbol:{symbol} Return in Period Time Saved".format(symbol=symbol))
        except:
            print(f"Symbol:{symbol} Return goes wrong".format(symbol=symbol))


def ticker_price_return_percentile_api(date):
    return_cols = ['price_return_7d',
                   'price_return_14d',
                   'price_return_30d',
                   'price_return_60d',
                   'price_return_90d',
                   'price_return_180d', ]
    cols = ['symbol'] + return_cols
    ticker_returns = TickerReturn.objects.filter(date=date)
    if len(ticker_returns) > 0:
        returns = [[r.symbol, r.price_return_7d, r.price_return_14d, r.price_return_30d,
                r.price_return_60d, r.price_return_90d, r.price_return_180d] for r in ticker_returns]
        returns = pd.DataFrame(returns, columns=cols)
        returns.set_index('symbol', inplace=True)
        for symbol in returns.index:
            percentiles = []
            for col in return_cols:
                percentile = stats.percentileofscore(returns[col], returns.loc[symbol, col])/100.0
                returns.loc[symbol, f'{col}_percentile'] = percentile
                percentiles.append(percentile)

            percentile = TickerPerformancePercentile(
                date=date,
                symbol=symbol,
                pr_7d_percentile=returns.loc[symbol, 'price_return_7d_percentile'],
                pr_14d_percentile=returns.loc[symbol, 'price_return_14d_percentile'],
                pr_30d_percentile=returns.loc[symbol, 'price_return_30d_percentile'],
                pr_60d_percentile=returns.loc[symbol, 'price_return_60d_percentile'],
                pr_90d_percentile=returns.loc[symbol, 'price_return_90d_percentile'],
                pr_180d_percentile=returns.loc[symbol, 'price_return_180d_percentile'],
                HandM=np.mean(percentiles)
            )
            try:
                percentile.save()
                print(f"Price Return Percentile:{symbol} saved successfully".format(symbol=symbol))
            except:
                print(f"Price Return Percentile:{symbol} goes wrong".format(symbol=symbol))
    else:
        print(f"Percentile: No data  ")
