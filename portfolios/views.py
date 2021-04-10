from users.models import CustomUser as User
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from portfolios.models import Portfolio
from portfolios.models import Position
from open_and_close.models import OpenClose
from portfolios.serializers import PortfolioSerializer
from datetime import datetime
import json
import math


@api_view(['POST'])
def portfolio_create(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        is_weights = True if body['is_weights'] else False
        user = User.objects.get(email=body['email'])
        symbols = body['symbols']
        if len(body['weights']) == len(body['symbols']):
            budgets = [body['total_budgets'] * body['weights'][i] for i in range(len(symbols))]

            if is_weights:
                portfolio = Portfolio(
                    user=user,
                    name=body['name'],
                    symbols=symbols,
                    weights=body['weights'],
                    budgets=budgets,
                    total_budget=body['total_budgets'],
                    start_date=body['start_date'],
                    end_date=body['end_date'],
                )

                try:
                    portfolio.save()
                except:
                    print("Portfolio Save wrong")
            else:
                portfolio = Portfolio(
                    user=user,
                    name=body['name'],
                    symbols=symbols,
                )

            the_portfolio = portfolio.objects.get(name=body['name'])

            for sid in range(len(symbols)):
                last_trade = OpenClose.objects.filter(symbol=symbols[sid], date__gte=datetime.now()).order_by('-date')[0]
                position = Position(
                    symbol=symbols[sid],
                    portfolio=the_portfolio,
                    user=user,
                    budget=round(body['total_budgets'] * body['weights'][sid], 5),
                    buy_price=last_trade.close,
                    shares=math.floor(body['total_budgets'] * body['weights'][sid]/last_trade.close)
                )

                position.save()

            return JsonResponse(body, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'weights and symbols number is not equal'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def portfolio_add_position(request):
    body = json.loads(request.body)
    name = body['name']
    symbol = body['symbol']
    buy_price = body['buy_price']
    is_unit = body['is_unit']
    budget = 1000.0 if is_unit else body['budget']
    user = User.objects.get(email=body['email'])

    _p = Portfolio.objects.get(name=name)
    _p.symbols = _p.symbols.append(body['symbol'])
    _p.budgets = _p.budgets.append(budget)
    _p.total_budget = _p.total_budget + budget
    _p.save()

    pos = Position(
        user=user,
        symbol=symbol,
        buy_price=buy_price,
        budget=budget,
        shares=round(budget/buy_price, 5),
    )

    pos.save()

    return JsonResponse({'message': 'add position'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def portfolio_list(request):
    if request.method == 'GET':
        ports = Portfolio.objects.all()

    portfolio_serializer = PortfolioSerializer(ports, many=True)
    return JsonResponse(portfolio_serializer.data, safe=False, )
