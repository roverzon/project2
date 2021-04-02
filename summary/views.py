from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from summary.services import candle_chart_technical_api
from summary.performance import custom_MACD
from datetime import datetime


@api_view(['GET'])
def candle_line_alert(request):
    date = request.GET['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    summary = candle_chart_technical_api(date=date)
    return JsonResponse({'candle_line_alert': summary},  status=status.HTTP_200_OK)


@api_view(['GET'])
def technical_indicator_MACD(request, symbol):
    date = request.GET['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    custom_MACD(symbol=symbol, date=date)
    return JsonResponse({'Technical Analysis': 'MACD analysis'},  status=status.HTTP_200_OK)
