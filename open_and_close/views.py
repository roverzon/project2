from django.http.response import JsonResponse
from rest_framework import status
from open_and_close.models import OpenClose
from open_and_close.tasks import polygon_tickers_open_and_close_async
from open_and_close.services import polygon_stock_previous_close
from tickers.models import Ticker
from open_and_close.serializers import OpenCloseSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from polygon import RESTClient


@api_view(['GET'])
@permission_classes([AllowAny])
def open_and_close_all_tickers_v3(request):
    if request.method == 'GET':
        white_list = ['BILI', 'PLTR']
        symbols = [(t.symbol,'2021-03-02', '2021-03-20') for t in Ticker.objects.all() if t.symbol in white_list]
        jobs = polygon_tickers_open_and_close_async.chunks(symbols, 10)
        jobs.apply_async()
        return JsonResponse({'message': 'open_and_close sent to the background'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def open_and_close_detail(request, symbol):
    if request.method == 'GET':
        open_and_close = OpenClose.objects.all()
        tdate = request.GET.get('date')

        if symbol is not None:
            open_and_close = open_and_close.filter(symbol__iexact=symbol, tdate__iexact=tdate)
            open_and_close_serializer = OpenCloseSerializer(open_and_close, many=True)
            return JsonResponse(open_and_close_serializer.data, safe=False, )


@api_view(['GET'])
def last_stock_open_and_close(request, symbol):
    if request.method == 'GET':
        polygon_stock_previous_close(symbol=symbol)
        return JsonResponse({'message': f'Symbol:{symbol} last data save'.format(symbol=symbol)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def snapshot_all_tickers(request):
    if request.method == 'GET':
        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
            rep = client.stocks_equities_snapshot_all_tickers()
            tickers = rep.tickers
            trades = [{t['ticker']: t['date']} for t in tickers ]

        return JsonResponse({'tickers': trades}, safe=False, )


