from django.db import models
from django.utils import timezone
from tickers.models import TickerDetail
from django.contrib.postgres.fields import ArrayField

class StockMarketIndex(models.Model):
    name = models.CharField('Stock Market Index', max_length=255)
    index_symbol = models.CharField(max_length=255)
    note = models.TextField()
    tags = ArrayField(models.CharField(max_length=100))
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class StockMarketIndexComponent(models.Model):
    symbol = models.CharField(max_length=255)
    weight = models.FloatField()
    market_index = models.ForeignKey(StockMarketIndex, on_delete=models.CASCADE)
    ticker_detail = models.ForeignKey(TickerDetail, on_delete=models.CASCADE)
    on_list = models.BooleanField(default=True)
    tags = ArrayField(models.CharField(max_length=100))
    company_count = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
