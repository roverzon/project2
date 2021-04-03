from django.db import models
from django.utils import timezone


class OpenClose(models.Model):
    date = models.DateTimeField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('date', 'symbol')


class JobRecord(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100, default='open_and_close')
    type = models.CharField(max_length=100, default='daily')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('date',)


class SnapShotDay(models.Model):
    date = models.DateTimeField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    volume_weighted = models.FloatField()

    class Meta:
        unique_together = ('date', 'symbol')


class TradeAgg(models.Model):
    date = models.BigIntegerField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    volume_weighted = models.FloatField()
    trans = models.IntegerField()

    class Meta:
        unique_together = ('date', 'symbol')
