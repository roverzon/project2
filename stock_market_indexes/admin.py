from django.contrib import admin
from .models import StockMarketIndex, StockMarketIndexComponent


admin.site.register(StockMarketIndex)
admin.site.register(StockMarketIndexComponent)
