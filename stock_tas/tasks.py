from djangoProject.celery import app
from stock_tas.services import cross_star_api, stock_linear_trending_api, stock_candle_pattern_api
from tickers.models import Ticker

@app.task
def cross_star_scanning_async(symbol, from_, end_):
    cross_star_api(symbol=symbol, from_=from_, end_=end_)


@app.task(name="ticker_trending_context_periodic")
def ticker_trending_context(date):
    symbols = [t.symbol for t in Ticker.objects.all()]
    for s in symbols:
        stock_linear_trending_api(symbol=s, date=date)


@app.task(name="ticker_candle_alert_periodic")
def ticker_candle_alert(date):
    symbols = [t.symbol for t in Ticker.objects.all()]
    for s in symbols:
        stock_candle_pattern_api(symbol=s, date=date)
