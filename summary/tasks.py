from djangoProject.celery import app
from summary.services import candle_chart_technical_api


@app.task
def candle_chart_alert(date):
    candle_chart_technical_api(date=date)
