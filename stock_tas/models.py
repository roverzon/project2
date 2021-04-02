from django.db import models
from django.utils import timezone


class InvertedHammerRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    close = models.FloatField(default=0.0)
    is_upper = models.BooleanField(default=False)
    is_down = models.BooleanField(default=False)
    is_lift = models.BooleanField(default=True)
    lift = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    volume_lift = models.FloatField(default=0.0)
    is_high_exchange = models.BooleanField(default=False)
    delta = models.FloatField(default=0.0)
    diff_time_delta = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')


class BlackLineRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    line_type= models.CharField(max_length=255, default='M')
    close = models.FloatField(default=0.0)
    price_lift = models.FloatField(default=0.0)
    is_upper = models.BooleanField(default=False)
    is_down = models.BooleanField(default=False)
    true_range = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    volume_lift = models.FloatField(default=0.0)
    is_high_exchange = models.BooleanField(default=False)
    range_threshold = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')


class RedLineRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    line_type= models.CharField(max_length=255, default='M')
    close = models.FloatField(default=0.0)
    price_lift = models.FloatField(default=0.0)
    is_upper = models.BooleanField(default=False)
    is_down = models.BooleanField(default=False)
    true_range = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    volume_lift = models.FloatField(default=0.0)
    is_high_exchange = models.BooleanField(default=False)
    range_threshold = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')


class GapRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    price_lift = models.FloatField(default=0.0)
    is_upper = models.BooleanField(default=False)
    range_threshold = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')


class TrendingRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    close = models.FloatField(default=0.0)
    slope = models.FloatField(default=0.0)
    angle = models.FloatField(default=0.0)
    sma_5d = models.FloatField(default=0.0)
    sma_10d = models.FloatField(default=0.0)
    sma_20d = models.FloatField(default=0.0)
    sma_30d = models.FloatField(default=0.0)
    cross_sma5 = models.FloatField(default=0.0)
    cross_sma10 = models.FloatField(default=0.0)
    cross_sma20 = models.FloatField(default=0.0)
    cross_sma30 = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')
