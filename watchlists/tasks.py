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
    for user in get_user_model().objects.all():
        ws = WatchList.objects.filter(user=user)
        if not ws:
            continue

        template = Template(REPORT_TEMPLATE)

        send_mail(
            'Your QuickPublisher Activity',
            template.render(context=Context({'posts': ws})),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )
