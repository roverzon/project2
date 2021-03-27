from open_and_close.services import polygon_open_and_close_api
from djangoProject.celery import app


@app.task
def polygon_tickers_open_and_close_async(symbol, from_, end_):
    polygon_open_and_close_api(symbol=symbol, from_=from_, end_=end_)
