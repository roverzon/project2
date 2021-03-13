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


class OpenCloseWN(models.Model):
    year = models.CharField(max_length=10)
    week_number = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('year', 'week_number', 'symbol')


class OpenCloseMonth(models.Model):
    year = models.CharField(max_length=10)
    month = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('year', 'month', 'symbol')

