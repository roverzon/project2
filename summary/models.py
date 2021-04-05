from django.db import models


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
