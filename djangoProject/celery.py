import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'updated last date at 5 a.m. every day': {
        'task': 'polygon_tickers_open_and_close_periodic',
        'schedule': crontab(hour=5, minute=0),
    },
}

app.conf.timezone = 'Asia/Shanghai'
