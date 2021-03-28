from open_and_close.services import polygon_open_and_close_api, polygon_stock_previous_close
from djangoProject.celery import app
from tickers.models import Ticker


@app.task
def polygon_tickers_open_and_close_async(symbol, from_, end_):
    polygon_open_and_close_api(symbol=symbol, from_=from_, end_=end_)


@app.task(name='polygon_tickers_open_and_close_periodic')
def polygon_tickers_open_and_close_periodic():
    symbols = [t.symbol for t in Ticker.objects.all()]
    for symbol in symbols:
        polygon_stock_previous_close(symbol=symbol)
