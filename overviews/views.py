from django.http.response import JsonResponse
from rest_framework import status
from overviews.models import Overview
from overviews.tasks import alpha_vantage_company_overview_async
from overviews.tasks import alpha_vantage_overview_api
from overviews.serializers import OverviewSerializer
from rest_framework.decorators import api_view


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
        return JsonResponse({'message': f'Overview:{symbol} save successflly'.format(symbol)},  status=status.HTTP_200_OK)


@api_view(['GET'])
def alpha_vantage_company_overview_aync(request, symbol):
    if request.method == 'GET':
        alpha_vantage_company_overview_async(symbol=symbol)
        return JsonResponse({'message': f'Overview:{symbol} sent to the background'.format(symbol)},  status=status.HTTP_200_OK)
