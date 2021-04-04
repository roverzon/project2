from django.http.response import JsonResponse
from rest_framework import status
from tickers.models import Ticker
from income_statements.models import Income
from income_statements.services import alpha_vantage_income_statement_api
from income_statements.tasks import alpha_vantage_income_statement_annualReport_async, \
    alpha_vantage_income_statement_quarterlyReport_async
from income_statements.serializers import IncomeSerializer
from rest_framework.decorators import api_view
from collections import OrderedDict
from random import sample


@api_view(['GET'])
def income_statement_init_async(request):
    is_sampled = True if request.GET.get('sampled') else False
    symbols = [(t.symbol, ) for t in Ticker.objects.all()]

    if is_sampled > 0:
        sample_num = 20
        symbols = sample(symbols, sample_num)
    else:
        symbols = symbols

    annual_jobs = alpha_vantage_income_statement_annualReport_async.chunks(symbols, 10)
    annual_jobs.apply_async()

    quarterly_jobs = alpha_vantage_income_statement_quarterlyReport_async.chunks(symbols, 10)
    quarterly_jobs.apply_async()

    return JsonResponse({'message': 'INCOME_STATEMENT AnnualReport: sent to the background'},status=status.HTTP_200_OK)


@api_view(['GET'])
def income_list(request):
    num_com = 0
    if request.method == 'GET':
        incomes = Income.objects.all()
        income_serializer = IncomeSerializer(incomes, many=True)
        return JsonResponse(income_serializer.data, safe=False,
                            status=status.HTTP_200_OK )

    elif request.method == 'DELETE':
        count = Income.objects.all().delete()
        return JsonResponse({'message': f'{num_com}Companies were deleted successfully!'.format(num_com=count[0])},
                            status=status.HTTP_200_OK)


@api_view(['GET'])
def symbol_income_list(request, symbol):
    if request.method == 'GET':
        incomes = Income.objects.all()
        income_T = OrderedDict()

        if symbol is not None:
            incomes = incomes.filter(symbol__iexact=symbol)

            income_T['fiscal_year'] = [income.fiscal_year for income in incomes]
            income_T['total_revenue'] = [income.total_revenue for income in incomes]
            income_T['total_operating_expense'] = [income.total_operating_expense for income in incomes]
            income_T['cost_of_revenue'] = [income.cost_of_revenue for income in incomes]
            income_T['gross_profit'] = [income.gross_profit for income in incomes]
            income_T['ebit'] = [income.ebit for income in incomes]
            income_T['net_income'] = [income.net_income for income in incomes]
            income_T['research_and_development'] = [income.research_and_development for income in incomes]
            income_T['effect_of_accounting_charges'] = [income.effect_of_accounting_charges for income in incomes]
            income_T['income_before_tax'] = [income.income_before_tax for income in incomes]
            income_T['minority_interest'] = [income.minority_interest for income in incomes]
            income_T['selling_general_administrative'] = [income.selling_general_administrative for income in incomes]
            income_T['other_non_operating_income'] = [income.other_non_operating_income for income in incomes]
            income_T['operating_income'] = [income.operating_income for income in incomes]
            income_T['other_operating_expense'] = [income.other_operating_expense for income in incomes]
            income_T['interest_expense'] = [income.interest_expense for income in incomes]
            income_T['tax_provision'] = [income.tax_provision for income in incomes]
            income_T['interest_income'] = [income.interest_expense for income in incomes]
            income_T['net_interest_income'] = [income.net_interest_income for income in incomes]
            income_T['extraordinary_items'] = [income.extraordinary_items for income in incomes]
            income_T['non_recurring'] = [income.non_recurring for income in incomes]
            income_T['other_items'] = [income.other_items for income in incomes]
            income_T['income_tax_expense'] = [income.income_tax_expense for income in incomes]
            income_T['total_other_income_expense'] = [income.total_other_income_expense for income in incomes]
            income_T['discontinued_operations'] = [income.discontinued_operations for income in incomes]
            income_T['net_income_from_continuing_operations'] = [income.net_income_from_continuing_operations for income in incomes]
            income_T['net_income_applicable_to_common_shares'] = [income.net_income_applicable_to_common_shares for income in incomes]
            income_T['preferred_stock_and_other_adjustments'] = [income.preferred_stock_and_other_adjustments for income in incomes]

            return JsonResponse(income_T, safe=False, )


@api_view(['GET'])
def symbol_income_detail(request, symbol, fyear):
    if request.method == 'GET':
        income = Income.objects.get(symbol=symbol, fiscal_year=fyear)
        income_serializer = IncomeSerializer(income)
        return JsonResponse(income_serializer.data)


@api_view(['GET'])
def alpha_vantage_income_statement_annual(request, symbol):
    if request.method == 'GET':
        alpha_vantage_income_statement_api(symbol=symbol, report_type='annualReports')
        return JsonResponse({'message': 'Annual Data Save successlly'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_income_statement_quarterly(request, symbol):
    if request.method == 'GET':
        alpha_vantage_income_statement_api(symbol=symbol, report_type='quarterlyReports')
        return JsonResponse({'message': 'Quarterly Data Save successlly'},  status=status.HTTP_200_OK)
