from djangoProject.celery import app
from income_statements.services import alpha_vantage_income_statement_api


@app.task
def alpha_vantage_income_statement_annualReport_async(symbol):
    alpha_vantage_income_statement_api(symbol=symbol, report_type='annualReports')


@app.task
def alpha_vantage_income_statement_quarterlyReport_async(symbol):
    alpha_vantage_income_statement_api(symbol=symbol, report_type='quarterlyReports')
