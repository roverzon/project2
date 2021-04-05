from financials.services import polygon_financial_api
from djangoProject.celery import app


@app.task
def polygon_financial_async(symbol):
    polygon_financial_api(symbol=symbol)
