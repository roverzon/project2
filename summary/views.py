from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from summary.services import candle_chart_technical_api
from datetime import datetime
from json import dumps


@api_view(['GET'])
def candle_line_alert(request):
    date = request.GET['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    summary = candle_chart_technical_api(date=date)
    return JsonResponse({'candle_line_alert': summary},  status=status.HTTP_200_OK)
