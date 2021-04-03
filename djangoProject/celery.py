import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

today = datetime.now().strftime('%Y-%m-%d')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'updated last date at 5 a.m. every day': {
        'task': 'polygon_tickers_open_and_close_periodic',
        'schedule': crontab(hour=5, minute=0),
        'args': (today,)
    },
    'candle line alert updated at 6:30 a.m. every day': {
        'task': 'ticker_candle_alert_periodic',
        'schedule': crontab(hour=6, minute=30),
        'args': (today,)
    },
    'trending context updated at 7:30 a.m. every day': {
        'task': 'ticker_trending_context_periodic',
        'schedule': crontab(hour=7, minute=30),
        'args': (today,)
    },
}

app.conf.timezone = 'Asia/Shanghai'
