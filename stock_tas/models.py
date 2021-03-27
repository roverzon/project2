from django.db import models
from django.utils import timezone


class CrossStarRecord(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=255)
    close = models.FloatField(default=0.0)
    is_star = models.BooleanField(default=True)
    is_lift = models.BooleanField(default=True)
    lift = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    volume_lift = models.FloatField(default=0.0)
    is_high_lift = models.BooleanField(default=False)
    delta = models.FloatField(default=0.0)
    diff_time_delta = models.FloatField(default=0.0)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        unique_together = ('date', 'symbol')
