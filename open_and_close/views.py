from django.http.response import JsonResponse
from rest_framework import status
from open_and_close.models import OpenClose
from open_and_close.tasks import tickers_all_open_and_close_async
from tickers.models import Ticker
from open_and_close.serializers import OpenCloseSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

from polygon import RESTClient
from datetime import datetime
from random import sample

import pandas as pd


@api_view(['GET'])
@permission_classes([AllowAny])
def open_and_close_all_tickers_v3(request):
    if request.method == 'GET':
        symbols = [(t.symbol,'2020-01-02', '2021-03-20') for t in Ticker.objects.all()]
        jobs = tickers_all_open_and_close_async.chunks(symbols, 10)
        jobs.apply_async()
        return JsonResponse({'message': 'send to background v3'},  status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def open_and_close_all_tickers(request):
    start_date = request.GET.get('from_')
    end_date = request.GET.get('end_')
    tickers = Ticker.objects.all()
    symbols = [ t.symbol for t in tickers if t.symbol == 'BILI']
    dates = pd.bdate_range(start=start_date, end=end_date)

    with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
        for symbol in symbols:
            for date in dates:
                    rep = client.stocks_equities_daily_open_close(symbol=symbol, date=date.strftime('%Y-%m-%d'))
                    if rep.symbol != '':
                        openAndClose = OpenClose(
                            symbol=symbol,
                            date=date,
                            open=rep.open,
                            high=rep.high,
                            low=rep.low,
                            close=rep.close,
                            afterHours=rep.after_hours,
                            preMarket=rep.preMarket,
                            volume=rep.volume
                        )
                        text = f"Symbol:{symbol} at date {date}".format(symbol=symbol, date=date)
                        print(text)
                        openAndClose.save()

    return JsonResponse({'message': 'Trading Data Save successfully'},  status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def open_and_close_detail_init(request, symbol):
    if request.method == 'GET':

        start_date = request.GET.get('from_')
        end_date = request.GET.get('end_')

        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')

        dates = pd.bdate_range(start=start_date, end=end_date)

        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
            for date in dates:
                rep = client.stocks_equities_daily_open_close(symbol=symbol, date=date.strftime('%Y-%m-%d'))
                if rep.symbol != '':
                    openAndClose = OpenClose(
                        symbol=symbol,
                        open=rep.open,
                        high=rep.high,
                        low=rep.low,
                        close=rep.close,
                        afterHours=rep.after_hours,
                        preMarket=rep.preMarket,
                        volume=rep.volume
                    )
                    try:
                        openAndClose.save()
                    except:
                        pass
                else:
                    pass

        return JsonResponse({'message': 'Trading Data Save successfully'},  status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def open_and_close_detail_init(request, symbol):

    if request.method == 'GET':
        start_date = request.GET.get('from_')
        end_date = request.GET.get('end_')

        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')

        dates = pd.bdate_range(start=start_date, end=end_date)
        whitelist = ['PDD', 'NIO', 'BILI', 'DAL']
        if len(whitelist) > 0:
            symbols = [t.symbol for t in Ticker.objects.all() if t.symbol in whitelist]
        else:
            symbols = [t.symbol for t in Ticker.objects.all()]

        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
            for symbol in symbols:
                for date in dates:
                    rep = client.stocks_equities_daily_open_close(symbol=symbol, date=date.strftime('%Y-%m-%d'))
                    if rep.symbol != '':
                        openAndClose = OpenClose(
                            symbol=symbol,
                            open=rep.open,
                            high=rep.high,
                            low=rep.low,
                            close=rep.close,
                            afterHours=rep.after_hours,
                            preMarket=rep.preMarket,
                            volume=rep.volume
                        )
                        try:
                            openAndClose.save()
                        except:
                            pass
                    else:
                        pass

        return JsonResponse({'message': 'Trading Data Save successfully'},  status=status.HTTP_200_OK)


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
def snapshot_all_tickers(request):
    if request.method == 'GET':
        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
            rep = client.stocks_equities_snapshot_all_tickers()
            tickers = rep.tickers
            trades = [{t['ticker']: t['date']} for t in tickers ]

        return JsonResponse({'tickers': trades }, safe=False, )

