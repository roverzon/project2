from django.http.response import JsonResponse
from stock_tas.services import cross_star
from stock_tas.tasks import cross_star_scanning_async
from tickers.models import Ticker
from rest_framework import status
from datetime import datetime
import pandas as pd


def scanner_cross_star(request, symbol):
    date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
    is_star = cross_star(symbol=symbol, date=date)
    return JsonResponse({'message': f'Ticker:{symbol} on {date} is corss star {is_star}'.
                        format(symbol=symbol, date=date, is_star=is_star)}, status=status.HTTP_200_OK)


def scan_ticker_cross_star(request):
    white_list = [('BLDP', ), ('BIDU', ), ('BE', ), ('TSLA', ),
                  ('PDD', ), ('PLTR', ), ('X',), ('SNOW', ),
                  ('TSM', ), ('SCCO', ), ('JD', ), ('INTC', ),
                  ('ADBE', ), ('SE', ), ('PYPL', ), ('BAC', )]
    # white_list = [('PLTR', )]
    dates = pd.bdate_range(start='2020-06-01', end='2021-03-27')
    for symbol in white_list:
        for pdate in dates:
            cross_star(symbol=symbol[0], date=pdate)

    return JsonResponse({'message': f'success'}, status=status.HTTP_200_OK)


def scan_ticker_cross_star_async(request):
    white_list = [('BLDP', '2020-06-01', '2021-03-27'), ('BIDU', '2020-06-01','2021-03-27'), ('BE', '2020-06-01','2021-03-27'), ('TSLA', '2020-06-01','2021-03-27'),
                  ('PDD', '2020-06-01', '2021-03-27'), ('PLTR','2020-06-01','2021-03-27' ), ('X','2020-06-01','2021-03-27'), ('SNOW', '2020-06-01','2021-03-27'),
                  ('TSM', '2020-06-01', '2021-03-27'), ('SCCO', '2020-06-01','2021-03-27'), ('JD', '2020-06-01','2021-03-27'), ('INTC', '2020-06-01','2021-03-27'),
                  ('ADBE', '2020-06-01', '2021-03-27'), ('SE', '2020-06-01','2021-03-27'), ('PYPL', '2020-06-01','2021-03-27'), ('BAC', '2020-06-01','2021-03-27')]

    # symbols = [(t.symbol,'2021-03-02', '2021-03-20') for t in Ticker.objects.all()]

    scanner_jobs = cross_star_scanning_async.chunks(white_list, 10)
    scanner_jobs.apply_async()
    return JsonResponse({'message': f'success'}, status=status.HTTP_200_OK)
