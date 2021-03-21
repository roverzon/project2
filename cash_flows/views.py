from django.http.response import JsonResponse
from rest_framework import status
from cash_flows.models import CashFlow, cash_flow_fields_map
from cash_flows.services import alpha_vantage_cash_flow_api
from tickers.models import Ticker
from cash_flows.serializers import CashFlowSerializer
from cash_flows.tasks import alphavantage_cashflow_annualReport_async, alphavantage_cashflow_quarterlyReport_async
from rest_framework.decorators import api_view, permission_classes
from collections import OrderedDict
from random import sample


@api_view(['GET'])
def func1(request):
    sample_num = 20
    symbols = [(t.symbol, ) for t in Ticker.objects.all()]
    if sample_num > 0:
        symbols = sample(symbols, sample_num)
    else:
        symbols = symbols
    jobs = alphavantage_cashflow_quarterlyReport_async.chunks(symbols, 10)
    jobs.apply_async()
    return JsonResponse({'message': 'sent to the background'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def cashflow_list(request):
    if request.method == 'GET':
        cashflows = CashFlow.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            cashflows = cashflows.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        cashflow_serializer = CashFlowSerializer(cashflows, many=True)
        return JsonResponse(cashflow_serializer.data, safe=False, )

    elif request.method == 'DELETE':
        count = CashFlow.objects.all().delete()
        return JsonResponse({'message': '{} Companies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def symbol_cashflow_list(request, symbol):
        if request.method == 'GET':
            cashflows = CashFlow.objects.filter(symbol=symbol)
            cashflowT = OrderedDict()
            cashflowT['reported_currency'] = [ cashflow.reported_currency for cashflow in cashflows ]
            cashflowT['fiscal_date_ending'] = [ cashflow.fiscal_date_ending for cashflow in cashflows ]
            cashflowT['investments'] = [ cashflow.investments for cashflow in cashflows ]
            cashflowT['change_in_liabilities'] = [ cashflow.change_in_liabilities for cashflow in cashflows ]
            cashflowT['cashflow_from_investment'] = [ cashflow.cashflow_from_investment for cashflow in cashflows ]
            cashflowT['other_cashflow_from_investment'] = [ cashflow.other_cashflow_from_investment for cashflow in cashflows ]
            cashflowT['net_borrowings'] = [ cashflow.net_borrowings for cashflow in cashflows ]
            cashflowT['cashflow_from_financing'] = [ cashflow.cashflow_from_financing for cashflow in cashflows ]
            cashflowT['other_cashflow_from_financing'] = [ cashflow.other_cashflow_from_financing for cashflow in cashflows ]
            cashflowT['change_in_operating_activities'] = [ cashflow.change_in_operating_activities for cashflow in cashflows ]
            cashflowT['net_income'] = [ cashflow.net_income for cashflow in cashflows ]
            cashflowT['change_in_cash'] = [ cashflow.change_in_cash for cashflow in cashflows ]
            cashflowT['operating_cashflow'] = [ cashflow.operating_cashflow for cashflow in cashflows ]
            cashflowT['other_operating_cashflow'] = [ cashflow.other_operating_cashflow for cashflow in cashflows ]
            cashflowT['depreciation'] = [ cashflow.depreciation for cashflow in cashflows ]
            cashflowT['dividend_payout'] = [ cashflow.dividend_payout for cashflow in cashflows ]
            cashflowT['stock_sale_and_purchase'] = [ cashflow.stock_sale_and_purchase for cashflow in cashflows ]
            cashflowT['change_in_inventory'] = [ cashflow.change_in_inventory for cashflow in cashflows ]
            cashflowT['change_in_account_receivables'] = [ cashflow.change_in_account_receivables for cashflow in cashflows ]
            cashflowT['change_in_net_income'] = [ cashflow.change_in_net_income for cashflow in cashflows ]
            cashflowT['capital_expenditures'] = [ cashflow.capital_expenditures for cashflow in cashflows ]
            cashflowT['change_in_receivables'] = [ cashflow.change_in_receivables for cashflow in cashflows ]
            cashflowT['change_in_exchange_rate'] = [ cashflow.change_in_exchange_rate for cashflow in cashflows ]
            cashflowT['change_in_cash_and_cash_equivalents'] = [ cashflow.change_in_cash_and_cash_equivalents for cashflow in cashflows ]
            return JsonResponse(cashflowT, safe=False,)



@api_view(['GET'])
def cashflow_detail(request, pk):
    try:
        cashflow = CashFlow.objects.get(pk=pk)

        if request.method == 'GET':
            cashflow_serializer = CashFlowSerializer(cashflow)
            return JsonResponse(cashflow_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def alpha_vantage_cashflow_annual(request, symbol):
    if request.method == 'GET':
        alpha_vantage_cash_flow_api(symbol=symbol, report_type='annualReports')
        return JsonResponse({'message': 'AlphaVantage Annual Report saved successfully'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_cashflow_quarterly(request, symbol):
    if request.method == 'GET':
        alpha_vantage_cash_flow_api(symbol=symbol, report_type='quarterlyReports')
        return JsonResponse({'message': 'AlphaVantage Quarterly Report saved successfully'},  status=status.HTTP_200_OK)
