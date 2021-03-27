from djangoProject.celery import app
from overviews.services import alpha_vantage_overview_api
from balance_statements.services import alpha_vantage_balance_sheet_api
from cash_flows.services import alpha_vantage_cash_flow_api
from income_statements.services import alpha_vantage_income_statement_api


@app.task
def alpha_vantage_company_overview_async(symbol):
    alpha_vantage_overview_api(symbol=symbol)


@app.task
def alpha_vantage_company_overview_and_financials_async(symbol):
    alpha_vantage_overview_api(symbol=symbol)

    alpha_vantage_balance_sheet_api(symbol=symbol, report_type='annualReports')
    alpha_vantage_balance_sheet_api(symbol=symbol, report_type='quarterlyReports')

    alpha_vantage_cash_flow_api(symbol=symbol, report_type='annualReports')
    alpha_vantage_cash_flow_api(symbol=symbol, report_type='quarterlyReports')

    alpha_vantage_income_statement_api(symbol=symbol, report_type='annualReports')
    alpha_vantage_income_statement_api(symbol=symbol, report_type='quarterlyReports')
