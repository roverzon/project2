from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Ticker(models.Model):
    symbol = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    locale = models.CharField(max_length=100)
    active = models.BooleanField()
    currency_name = models.CharField(max_length=100)
    cik = models.CharField(max_length=100)
    composite_figi = models.CharField(max_length=100)
    share_class_figi = models.CharField(max_length=100)
    last_updated_utc = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)


class TickerDetail(models.Model):
    symbol = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)
    exchangeSymbol = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    tags = ArrayField(models.CharField(max_length=100))
    similar = ArrayField(models.CharField(max_length=100))
    active = models.BooleanField()
    list_date = models.DateTimeField()
    updated_date = models.DateTimeField()


class TickerNews(models.Model):
    symbol = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    source = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
