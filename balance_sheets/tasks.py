from djangoProject.celery import app
from balance_sheets.services import alpha_vantage_balance_sheet_api


@app.task
def alpha_vantage_balance_sheet_annualReport_async(symbol):
    alpha_vantage_balance_sheet_api(symbol=symbol, report_type='annualReports')


@app.task
def alpha_vantage_balance_sheet_quarterlyReport_async(symbol):
    alpha_vantage_balance_sheet_api(symbol=symbol, report_type='quarterlyReports')
