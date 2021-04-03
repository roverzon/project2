from open_and_close.services import polygon_open_and_close_api, polygon_stock_previous_close, polygon_open_and_close_daily_api
from open_and_close.models import JobRecord
from tickers.models import Ticker
from djangoProject.celery import app
from tickers.models import Ticker
import pandas as pd


@app.task(name='polygon_tickers_open_and_close_async')
def polygon_tickers_open_and_close_async(symbol, from_, end_):
    polygon_open_and_close_api(symbol=symbol, from_=from_, end_=end_)


@app.task(name='polygon_tickers_open_and_close_prev_periodic')
def polygon_tickers_open_and_close_prev_periodic(date):
    if JobRecord.objects.filter(date=date).exists():
        print(f"market open_and_close data on {date} is updated".format(date=date))
    else:
        symbols = [t.symbol for t in Ticker.objects.all()]
        for symbol in symbols:
            polygon_stock_previous_close(symbol=symbol)


@app.task(name='polygon_tickers_open_and_close_all_daily_updated_periodic')
def polygon_tickers_open_and_close_daily_all_updated(from_, to_):
    records = JobRecord.objects.filter(name="open_and_close", type='daily')
    dates = set([t.strftime('%Y-%m-%d') for t in pd.bdate_range(start=from_, end=to_)])
    symbols = [t.symbol for t in Ticker.objects.all()]

    if len(records) > 0:
        record_date = set([record.date for record in records])
        needed_date = dates.difference(record_date)
    else:
        needed_date = dates

    for date in needed_date:
        for symbol in symbols:
            polygon_open_and_close_daily_api(symbol=symbol, date=date)


@app.task(name='polygon_tickers_open_and_close_daily_updated_periodic')
def polygon_tickers_open_and_close_daily_updated(symbol, from_, to_):
    records = JobRecord.objects.filter(name="open_and_close", type='daily')
    dates = set([t.strftime('%Y-%m-%d') for t in pd.bdate_range(start=from_, end=to_)])

    if len(records) > 0:
        record_date = set([record.date for record in records])
        needed_date = dates.difference(record_date)
    else:
        needed_date = dates

    for date in needed_date:
        polygon_open_and_close_daily_api(symbol=symbol, date=date)
