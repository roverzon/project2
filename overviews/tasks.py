from djangoProject.celery import app
from overviews.services import alpha_vantage_overview_api


@app.task
def alpha_vantage_company_overview_async(symbol):
    alpha_vantage_overview_api(symbol=symbol)

