from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from virtual_accounts.models import VirtualAccount


class Portfolio(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    tags = ArrayField(models.CharField(max_length=100))
    virtual_account = models.ForeignKey(VirtualAccount, on_delete=models.CASCADE)
    symbols = ArrayField(models.CharField(max_length=10))
    weights = ArrayField(models.FloatField())
    budgets = ArrayField(models.FloatField())
    win_rate = models.FloatField(default=0.0)
    odds = models.FloatField(default=0.0)
    periods = models.FloatField(default=0.0)
    total_budget = models.FloatField()
    start_date = models.DateTimeField()
    expected_sold_date = models.DateTimeField()
    end_date = models.DateTimeField()
    portfolio_tags = ArrayField(models.CharField(max_length=10))
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)


