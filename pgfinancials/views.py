from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from pgfinancials.services import polygon_financial_api
from pgfinancials.tasks import polygon_financial_async


@api_view(['GET'])
@permission_classes([AllowAny])
def ticker_financial(request, symbol):
    if request.method == 'GET':
        polygon_financial_api(symbol=symbol)
        msg = f'Symbol: {symbol} Financial is saved '.format(symbol=symbol)
        return JsonResponse({'message': msg},  status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def ticker_financial_async(request, symbol):
    polygon_financial_async.delay(symbol)
    msg = f'Symbol: {symbol} Polygon Financial is sent to the background '.format(symbol=symbol)
    return JsonResponse({'message': msg},  status=status.HTTP_200_OK)

