from django.http.response import JsonResponse
from rest_framework import status
from balance_sheets.services import alpha_vantage_balance_sheet_api
from balance_sheets.models import BalanceSheet
from balance_sheets.tasks import alpha_vantage_balance_sheet_annualReport_async, \
    alpha_vantage_balance_sheet_quarterlyReport_async
from balance_sheets.serializers import BalanceSheetSerializer
from tickers.models import Ticker
from rest_framework.decorators import api_view
from collections import OrderedDict
from random import sample


@api_view(['GET'])
def balance_sheet_init_async(request):
    is_sampled = True if request.GET.get('sampled') else False
    symbols = [(t.symbol, ) for t in Ticker.objects.all()]

    if is_sampled:
        sample_num = 20
        symbols = sample(symbols, sample_num)
    else:
        symbols = symbols

    annual_jobs = alpha_vantage_balance_sheet_annualReport_async.chunks(symbols, 10)
    annual_jobs.apply_async()

    quarterly_jobs = alpha_vantage_balance_sheet_quarterlyReport_async.chunks(symbols, 10)
    quarterly_jobs.apply_async()

    return JsonResponse({'message': 'BALANCE_SHEET AnnualReport: sent to the background'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def balance_sheet_list(request):
    if request.method == 'GET':
        balancesheets = BalanceSheet.objects.all()

        symbol = request.GET.get('symbol', None)
        if symbol is not None:
            balancesheets = balancesheets.filter(symbol__icontains=symbol, status=status.HTTP_200_OK)

        balancesheet_serializer = BalanceSheetSerializer(balancesheets, many=True)
        return JsonResponse(balancesheet_serializer.data, safe=False, )


@api_view(['GET'])
def symbol_balance_sheet_list(request, symbol):
    if request.method == 'GET':
        balancesheetT = OrderedDict()
        if symbol is not None:
            balancesheets = BalanceSheet.objects.filter(symbol=symbol)
            balancesheetT['fiscal_date_ending'] = [ balancesheet.fiscal_date_ending for balancesheet in balancesheets ]
            balancesheetT['fiscal_year'] = [ balancesheet.fiscal_year for balancesheet in balancesheets ]
            balancesheetT['reported_currency'] = [ balancesheet.reported_currency for balancesheet in balancesheets ]
            balancesheetT['total_assets'] = [ balancesheet.total_assets for balancesheet in balancesheets ]
            balancesheetT['intangible_assets'] = [ balancesheet.intangible_assets for balancesheet in balancesheets ]
            balancesheetT['earning_assets'] = [ balancesheet.earning_assets for balancesheet in balancesheets ]
            balancesheetT['other_current_assets'] = [ balancesheet.other_current_assets for balancesheet in balancesheets ]
            balancesheetT['total_liabilities'] = [ balancesheet.total_liabilities for balancesheet in balancesheets ]
            balancesheetT['total_shareholder_equity'] = [ balancesheet.total_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_liabilities'] = [ balancesheet.deferred_long_term_liabilities for balancesheet in balancesheets ]
            balancesheetT['other_current_liabilities'] = [ balancesheet.other_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['common_stock'] = [ balancesheet.common_stock for balancesheet in balancesheets ]
            balancesheetT['retained_earnings'] = [ balancesheet.retained_earnings for balancesheet in balancesheets ]
            balancesheetT['other_liabilities'] = [ balancesheet.other_liabilities for balancesheet in balancesheets ]
            balancesheetT['goodwill'] = [ balancesheet.goodwill for balancesheet in balancesheets ]
            balancesheetT['other_assets'] = [ balancesheet.other_assets for balancesheet in balancesheets ]
            balancesheetT['cash'] = [ balancesheet.cash for balancesheet in balancesheets ]
            balancesheetT['total_current_liabilities'] = [ balancesheet.total_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['short_term_debt'] = [ balancesheet.short_term_debt for balancesheet in balancesheets ]
            balancesheetT['current_long_term_debt'] = [ balancesheet.current_long_term_debt for balancesheet in balancesheets ]
            balancesheetT['other_shareholder_equity'] = [ balancesheet.other_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['property_plant_equipment'] = [ balancesheet.property_plant_equipment for balancesheet in balancesheets ]
            balancesheetT['total_current_assets'] = [ balancesheet.total_current_assets for balancesheet in balancesheets ]
            balancesheetT['long_term_investment'] = [ balancesheet.long_term_investment for balancesheet in balancesheets ]
            balancesheetT['net_tangible_assets'] = [ balancesheet.net_tangible_assets for balancesheet in balancesheets ]
            balancesheetT['short_term_investment'] = [ balancesheet.short_term_investment for balancesheet in balancesheets ]
            balancesheetT['net_receivables'] = [ balancesheet.net_receivables for balancesheet in balancesheets ]
            balancesheetT['long_term_debt'] = [ balancesheet.long_term_debt for balancesheet in balancesheets ]
            balancesheetT['inventory'] = [ balancesheet.inventory for balancesheet in balancesheets ]
            balancesheetT['accounts_payable'] = [ balancesheet.accounts_payable for balancesheet in balancesheets ]
            balancesheetT['total_permanent_equity'] = [ balancesheet.total_permanent_equity for balancesheet in balancesheets ]
            balancesheetT['additional_paid_in_capital'] = [ balancesheet.additional_paid_in_capital for balancesheet in balancesheets ]
            balancesheetT['common_stock_total_equity'] = [ balancesheet.common_stock_total_equity for balancesheet in balancesheets ]
            balancesheetT['preferred_stock_total_equity'] = [ balancesheet.preferred_stock_total_equity for balancesheet in balancesheets ]
            balancesheetT['retained_earnings_total_equity'] = [ balancesheet.retained_earnings_total_equity for balancesheet in balancesheets ]
            balancesheetT['treasury_stock'] = [ balancesheet.treasury_stock for balancesheet in balancesheets ]
            balancesheetT['accumulated_amortization'] = [ balancesheet.accumulated_amortization for balancesheet in balancesheets ]
            balancesheetT['other_non_current_assets'] = [ balancesheet.other_non_current_assets for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_aseet_charges'] = [ balancesheet.deferred_long_term_aseet_charges for balancesheet in balancesheets ]
            balancesheetT['total_non_current_assets'] = [ balancesheet.total_non_current_assets for balancesheet in balancesheets ]
            balancesheetT['capital_lease_obligations'] = [ balancesheet.capital_lease_obligations for balancesheet in balancesheets ]
            balancesheetT['total_long_term_debt'] = [ balancesheet.total_long_term_debt for balancesheet in balancesheets ]
            balancesheetT['other_non_current_liabilities'] = [ balancesheet.other_non_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['deferred_long_term_asset_charges'] = [ balancesheet.deferred_long_term_asset_charges for balancesheet in balancesheets ]
            balancesheetT['total_non_current_liabilities'] = [ balancesheet.total_non_current_liabilities for balancesheet in balancesheets ]
            balancesheetT['negative_goodwill'] = [ balancesheet.negative_goodwill for balancesheet in balancesheets ]
            balancesheetT['warrants'] = [ balancesheet.warrants for balancesheet in balancesheets ]
            balancesheetT['preferred_stock_redeemable'] = [ balancesheet.preferred_stock_redeemable for balancesheet in balancesheets ]
            balancesheetT['capital_surplus'] = [ balancesheet.capital_surplus for balancesheet in balancesheets ]
            balancesheetT['liabilities_and_shareholder_equity'] = [ balancesheet.liabilities_and_shareholder_equity for balancesheet in balancesheets ]
            balancesheetT['cash_and_short_term_investments'] = [ balancesheet.cash_and_short_term_investments for balancesheet in balancesheets ]
            balancesheetT['accumulated_depreciation'] = [ balancesheet.accumulated_depreciation for balancesheet in balancesheets ]
            balancesheetT['common_stock_shares_outstanding'] = [ balancesheet.common_stock_shares_outstanding for balancesheet in balancesheets ]

    return JsonResponse(balancesheetT, safe=False, )


@api_view(['GET'])
def balance_sheet_detail(request, pk):
    try:
        balancesheet = BalanceSheet.objects.get(pk=pk)

        if request.method == 'GET':
            balancesheet_serializer = BalanceSheetSerializer(balancesheet)
            return JsonResponse(balancesheet_serializer.data)

    except:
        return JsonResponse({'message': 'The company does not exist'},  status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def alpha_vantage_balance_sheet_annual(request, symbol):
    if request.method == 'GET':
        alpha_vantage_balance_sheet_api(symbol=symbol, report_type='annualReports')
        return JsonResponse({'message': 'Annual Balance Sheet Data Save successlly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_balance_sheet_quarterly(request, symbol):
    if request.method == 'GET':
        alpha_vantage_balance_sheet_api(symbol=symbol, report_type='quarterlyReports')
        return JsonResponse({'message': 'Quarterly Balance Sheet Data Save successlly'},  status=status.HTTP_200_OK)
