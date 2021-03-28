from django.http.response import JsonResponse
from rest_framework import status
from tickers.models import Ticker
from open_and_close.tasks import polygon_tickers_open_and_close_async
from overviews.models import Overview
from overviews.tasks import alpha_vantage_company_overview_async, alpha_vantage_company_overview_and_financials_async
from overviews.tasks import alpha_vantage_overview_api
from overviews.serializers import OverviewSerializer
from balance_sheets.tasks import alpha_vantage_balance_sheet_annualReport_async, alpha_vantage_balance_sheet_quarterlyReport_async
from cash_flows.tasks import alpha_vantage_cashflow_annualReport_async, alpha_vantage_cashflow_quarterlyReport_async
from income_statements.tasks import alpha_vantage_income_statement_annualReport_async, alpha_vantage_income_statement_quarterlyReport_async
from pgfinancials.tasks import polygon_financial_async
from rest_framework.decorators import api_view
from random import sample


@api_view(['GET'])
def overview_init(request):
    from_ = '2020-06-01'
    end_ = '2021-03-27'
    white_list = [('BLDP', ), ('BIDU', ), ('BE', ), ('TSLA', ),
                  ('PDD', ), ('PLTR', ), ('XPEV',), ('SNOW', ),
                  ('TSM', ), ('SCCO', ), ('JD', ), ('INTC', ),
                  ('ADBE', ), ('SE', ), ('PYPL', ), ('BAC', ), ('JPM', ), ('NIO', ), ('LI', )]

    is_sampled = True
    if is_sampled:
        symbols = sample([(t.symbol, ) for t in Ticker.objects.all()], 20)
        symbols.extend(white_list)
    else:
        symbols = [(t.symbol, ) for t in Ticker.objects.all()]

    trading = [(s[0], from_, end_) for s in symbols]

    '''
        Alpha Vantage Overview data
    '''
    # overview_jobs = alpha_vantage_company_overview_async.chunks(symbols, 10)
    # overview_jobs.apply_async()

    '''
        Alpha Vantage Balance Sheet data
    '''
    # balance_sheet_annual_jobs = alpha_vantage_balance_sheet_annualReport_async.chunks(symbols, 10)
    # balance_sheet_quarterly_jobs = alpha_vantage_balance_sheet_quarterlyReport_async.chunks(symbols, 10)
    # balance_sheet_annual_jobs.apply_async()
    # balance_sheet_quarterly_jobs.apply_async()

    '''
        Alpha Vantage Cash Flow Sheet data
    '''
    # cash_flow_annual_jobs = alpha_vantage_cashflow_annualReport_async.chunks(symbols, 10)
    # cash_flow_quarterly_jobs = alpha_vantage_cashflow_quarterlyReport_async.chunks(symbols, 10)
    # cash_flow_annual_jobs.apply_async()
    # cash_flow_quarterly_jobs.apply_async()

    '''
        Alpha Vantage Income Statement Sheet data
    '''
    # income_statement_annual_jobs = alpha_vantage_income_statement_annualReport_async.chunks(symbols, 10)
    # income_statement_quarterly_jobs = alpha_vantage_income_statement_quarterlyReport_async.chunks(symbols, 10)
    # income_statement_annual_jobs.apply_async()
    # income_statement_quarterly_jobs.apply_async()

    '''
        Polygon Financials data
    '''
    # polygon_financial_jobs = polygon_financial_async.chunks(symbols, 10)
    # polygon_financial_jobs.apply_async()

    '''
        Polygon Trading data
    '''
    open_and_close_job = polygon_tickers_open_and_close_async.chunks(trading, 10)
    open_and_close_job.apply_async()

    return JsonResponse({'message': 'sent to background'},  status=status.HTTP_200_OK)



@api_view(['GET'])
def overview_list(request):
    if request.method == 'GET':
        companies = Overview.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            companies = companies.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        companies_serializer = OverviewSerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False, )


@api_view(['GET'])
def overview_detail(request, symbol):
    try:
        company = Overview.objects.get(symbol=symbol)

        if request.method == 'GET':
            company_serializer = OverviewSerializer(company)
            return JsonResponse(company_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def alpha_vantage_company_overview(request, symbol):
    if request.method == 'GET':
        alpha_vantage_overview_api(symbol=symbol)
        return JsonResponse({'message': f'Overview:{symbol} save successflly'.format(symbol=symbol)},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_company_overview_v2(request, symbol):
    if request.method == 'GET':
        alpha_vantage_company_overview_async(symbol=symbol)
        return JsonResponse({'message': f'Overview:{symbol} sent to the background'.format(symbol=symbol)},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_company_overview_and_financials(request, symbol):
    if request.method == 'GET':
        alpha_vantage_company_overview_and_financials_async(symbol)
        return JsonResponse({'message': f'{symbol} overview and financials sent to the background'.format(symbol=symbol)},  status=status.HTTP_200_OK)


