from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from financials.services import polygon_financial_api, polygon_financial_percentile_api
from financials.tasks import polygon_financial_async
from tickers.models import Ticker
from tickers.banchmark_list import get_white_list


@api_view(['GET'])
def polygon_tickers_financial_async(request):
    if request.method == 'GET':
        is_white = True if request.GET.get('white_list') else False
        if is_white:
            white_list_symbols = get_white_list()['symbols']
            symbols = [(t.symbol,) for t in Ticker.objects.all() if t.symbol in white_list_symbols]
        else:
            symbols = [(t.symbol,) for t in Ticker.objects.all() if t.symbol]

        financial_jobs = polygon_financial_async.chunks(symbols, 10)
        financial_jobs.apply_async()

        return JsonResponse({'message': 'open_and_close sent to the background'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def polygon_tickers_financial_percentile(request):
    if request.method == 'GET':
        is_white = True
        if is_white:
            white_list_symbols = get_white_list()['symbols']
            symbols = [t.symbol for t in Ticker.objects.all() if t.symbol in white_list_symbols]
        else:
            symbols = [t.symbol for t in Ticker.objects.all() if t.symbol]
        polygon_financial_percentile_api(symbols=symbols)

    return JsonResponse({'message': 'open_and_close sent to the background'},  status=status.HTTP_200_OK)




@api_view(['GET'])
@permission_classes([AllowAny])
def ticker_financial(request, symbol):
    if request.method == 'GET':
        polygon_financial_api(symbol=symbol)
        msg = f'Symbol: {symbol} Financial is saved '.format(symbol=symbol)
        return JsonResponse({'message': msg},  status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def ticker_financial_async(request, symbol):
    polygon_financial_async.delay(symbol)
    msg = f'Symbol: {symbol} Polygon Financial is sent to the background '.format(symbol=symbol)
    return JsonResponse({'message': msg},  status=status.HTTP_200_OK)

