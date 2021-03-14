from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from djangoProject.celery import app
from watchlists.models import WatchList

REPORT_TEMPLATE = """
Here's how you did till now:
 
{% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |
 
{% endfor %}
"""


@app.task
def send_watchlist_report():
    print('run run run')
