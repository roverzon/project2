from django.db import models
from django.utils import timezone


class TickerReturn(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10, blank=False)
    price_return_7d = models.FloatField()
    price_return_14d = models.FloatField()
    price_return_30d = models.FloatField()
    price_return_60d = models.FloatField()
    price_return_90d = models.FloatField()
    price_return_180d = models.FloatField()

    class Meta:
        unique_together = ('date', 'symbol')


class TickerPerformancePercentile(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10, blank=False)
    timeframe = models.CharField(max_length=20, blank=False, default='daily')
    performance_type = models.CharField(max_length=20, blank=False, default='trade')
    pr_7d_percentile = models.FloatField()
    pr_14d_percentile = models.FloatField()
    pr_30d_percentile = models.FloatField()
    pr_60d_percentile = models.FloatField()
    pr_90d_percentile = models.FloatField()
    pr_180d_percentile = models.FloatField()
    HandM = models.FloatField(default=0.0)

    class Meta:
        unique_together = ('date', 'symbol')


class TickerValuePercentile(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10, blank=False)
    timeframe = models.CharField(max_length=20, blank=False, default='daily')
    performance_type = models.CharField(max_length=20, blank=False, default='trade')
    value_fields1 = models.FloatField(default=0.0)
    value_fields2 = models.FloatField(default=0.0)
    value_fields3 = models.FloatField(default=0.0)
    value_fields4 = models.FloatField(default=0.0)
    value_fields5 = models.FloatField(default=0.0)
    value_fields6 = models.FloatField(default=0.0)
    value_fields7 = models.FloatField(default=0.0)
    value_fields8 = models.FloatField(default=0.0)
    value_score = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')
