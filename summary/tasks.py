from djangoProject.celery import app
from summary.services import candle_chart_technical_api, ticker_price_return_api
from datetime import datetime


@app.task(name="candle_chart_alert_period")
def candle_chart_alert_period():
    date = datetime.strptime('2020-11-18', '%Y-%m-%d')
    summary = candle_chart_technical_api(date=date)


@app.task(name='ticker_price_return_period')
def ticker_price_return_period():
    ticker_price_return_api(is_sampled=True)
