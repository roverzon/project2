from stock_tas.models import RedLineRecord, InvertedHammerRecord, BlackLineRecord


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
