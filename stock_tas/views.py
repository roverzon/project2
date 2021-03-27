from django.http.response import JsonResponse
from stock_tas.services import cross_star
from rest_framework import status
from datetime import datetime


def scanner_cross_star(request, symbol):
    date = datetime.strptime(request.GET['date'], '%Y-%m-%d')
    is_star = cross_star(symbol=symbol, date=date)
    return JsonResponse({'message': f'Ticker:{symbol} on {date} is corss star {is_star}'.
                        format(symbol=symbol, date=date, is_star=is_star)}, status=status.HTTP_200_OK)
