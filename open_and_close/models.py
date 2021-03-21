from django.db import models


class OpenClose(models.Model):
    date = models.DateTimeField()
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()
    afterHours = models.FloatField()
    preMarket = models.FloatField()

    class Meta:
        unique_together = ('date', 'symbol')


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
