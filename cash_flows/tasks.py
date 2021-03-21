from djangoProject.celery import app
from cash_flows.services import alpha_vantage_cash_flow_api

@app.task
def alpha_vantage_cashflow_annualReport_async(symbol):
    alpha_vantage_cash_flow_api(symbol=symbol, report_type='annualReports')

@app.task
def alpha_vantage_cashflow_quarterlyReport_async(symbol):
    alpha_vantage_cash_flow_api(symbol=symbol, report_type='quarterlyReports')
