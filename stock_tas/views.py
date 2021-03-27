from django.http.response import JsonResponse
from stock_tas.services import cross_star
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
