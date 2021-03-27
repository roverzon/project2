from django.http.response import JsonResponse
from multiprocessing import Pool
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime
from polygon import RESTClient
from tickers.models import Ticker, TickerDetail
from tickers.tasks import tickers_all_detail
import requests


@api_view(['GET'])
@permission_classes([AllowAny])
def polygon_all_tickers(request):
    default_host = 'https://api.polygon.io'
    polygon_url = default_host + '/vX/reference/tickers?limit=500&apiKey='
    apiKey = 'u8arVdihlX_6p_pRuvRUwa94YmI4Zrny'

    url = polygon_url + apiKey

    limit_query_times = 30
    ncount = 0
    next_page_path = ''
    rest = 0
    all_tickers = []

    with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:

        for t in range(limit_query_times):
            if ncount == 0:
                rep = requests.get(url).json()
                next_page_path = rep['next_page_path']
                all_tickers.extend(rep['results'])
            else:
                url = default_host + next_page_path
                rep = requests.get(url).json()
                all_tickers.extend(rep['results'])
                if rest > 0 and 'next_page_path' in rep:
                    next_page_path = rep['next_page_path']
                else:
                    break
            print(next_page_path)

            rest = limit_query_times - ncount
            ncount += 1

            for t in all_tickers:
                cik = t['cik'] if 'cik' in t else ''
                composite_figi = t['composite_figi'] if 'composite_figi' in t else ''
                share_class_figi = t['share_class_figi'] if 'share_class_figi' in t else ''
                currency_name = t['currency_name'] if 'currency_name' in t else ''

                ticker = Ticker(
                    symbol=t['ticker'],
                    name=t['name'],
                    market=t['market'],
                    locale=t['locale'],
                    active=t['active'],
                    cik=cik,
                    composite_figi=composite_figi,
                    share_class_figi=share_class_figi,
                    currency_name=currency_name,
                    last_updated_utc=t['last_updated_utc'],
                    created_at=datetime.now().strftime('%Y-%m-%d')
                )

                try:
                    ticker.save()
                    print(f"Ticker:{ticker} detail is saved".format(ticker=t['ticker']))
                except:
                    pass

                try:
                    rep_detail = client.reference_ticker_details(symbol=t['ticker'])
                    if rep_detail.sector is not None:
                        tickerS = Ticker.objects.get(symbol=t['ticker'])
                        ticker_detail = TickerDetail(
                            ticker=tickerS,
                            exchange=rep_detail.exchange,
                            exchangeSymbol=rep_detail.exchange,
                            industry=rep_detail.industry,
                            sector=rep_detail.sector,
                            tags=rep_detail.tags,
                            similar=rep_detail.similar,
                            list_date=rep_detail.listdate,
                            updated_date=datetime.strptime(rep_detail.updated, '%d/%M/%Y').strftime('%Y-%m-%d')
                        )
                        ticker_detail.save()
                except:
                    pass

    return JsonResponse({'message': 'query all tickers from Polygon.io'},  status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def polygon_all_tickers_v2(request):
    tickers_all_detail.delay()
    return JsonResponse({'message': 'send to background'},  status=status.HTTP_200_OK)


@api_view(['GET'])
def polygon_ticker_detail(request, symbol):
    if request.method == 'GET':
        with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:

            rep = client.reference_ticker_details(symbol=symbol)
            if rep.sector is not None:
                ticker = Ticker.objects.get(symbol=symbol)
                ticker_detail = TickerDetail(
                    ticker=ticker,
                    exchange=rep.exchange,
                    exchangeSymbol=rep.exchange,
                    industry=rep.industry,
                    sector=rep.sector,
                    tags=rep.tags,
                    similar=rep.similar,
                    list_date=rep.listdate,
                    updated_date=datetime.strptime(rep.updated, '%d/%M/%Y').strftime('%Y-%m-%d')
                )
                ticker_detail.save()

        return JsonResponse({'message': 'GET Ticker Detail Successfully'},  status=status.HTTP_200_OK)
