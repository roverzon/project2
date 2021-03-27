from django.http.response import JsonResponse
from rest_framework import status
from tickers.models import Ticker
from pgfinancials.models import Financial
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from pgfinancials.services import polygon_financial_api
from polygon import RESTClient
from random import sample


@api_view(['GET'])
@permission_classes([AllowAny])
def ticker_financial(request, symbol):
    if request.method == 'GET':
        polygon_financial_api(symbol=symbol)
        return JsonResponse({'message': f'Symbol: {symbol} Financial is saved '.format(symbol)},  status=status.HTTP_200_OK)
