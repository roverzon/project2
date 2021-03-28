from django.http.response import JsonResponse
from stock_tas.services import label_inverted_hammer_pattern, black_line
from stock_tas.tasks import cross_star_scanning_async
from tickers.models import Ticker
from rest_framework import status
from datetime import datetime
import pandas as pd


white_list = [('BLDP', '2020-06-01', '2021-03-27'), ('BIDU', '2020-06-01','2021-03-27'), ('BE', '2020-06-01','2021-03-27'), ('TSLA', '2020-06-01','2021-03-27'),
              ('PDD', '2020-06-01', '2021-03-27'), ('PLTR','2020-06-01','2021-03-27' ), ('X','2020-06-01','2021-03-27'), ('SNOW', '2020-06-01','2021-03-27'),
              ('TSM', '2020-06-01', '2021-03-27'), ('SCCO', '2020-06-01','2021-03-27'), ('JD', '2020-06-01','2021-03-27'), ('INTC', '2020-06-01','2021-03-27'),
              ('ADBE', '2020-06-01', '2021-03-27'), ('SE', '2020-06-01','2021-03-27'), ('PYPL', '2020-06-01','2021-03-27'), ('BAC', '2020-06-01','2021-03-27')]


def find_ticker_inverted_hammer(request, symbol):
    date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
    is_star = label_inverted_hammer_pattern(symbol=symbol, date=date)
    return JsonResponse({'message': f'Ticker:{symbol} on {date} is corss star {is_star}'.
                        format(symbol=symbol, date=date, is_star=is_star)}, status=status.HTTP_200_OK)


def scan_tickers_inverted_hammer(request):
    symbols = [(t.symbol, ) for t in white_list]
    dates = pd.bdate_range(start='2020-06-01', end='2021-03-27')
    for symbol in symbols:
        for pdate in dates:
            label_inverted_hammer_pattern(symbol=symbol[0 ], date=pdate)
    return JsonResponse({'message': f'success'}, status=status.HTTP_200_OK)


def scan_tickers_inverted_hammer_async(request):
    scanner_jobs = cross_star_scanning_async.chunks(white_list, 10)
    scanner_jobs.apply_async()
    return JsonResponse({'message': f'success'}, status=status.HTTP_200_OK)


def scan_ticker_black_line(request):
    symbols = [(t.symbol, ) for t in white_list]
    dates = pd.bdate_range(start='2020-06-01', end='2021-03-27')
    for symbol in symbols:
        for pdate in dates:
            black_line(symbol=symbol[0], date=pdate)

    return JsonResponse({'message': f'success'}, status=status.HTTP_200_OK)
