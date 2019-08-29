from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from celery.task.schedules import crontab
from .models import Notification
from .functions import send_notification
from datetime import datetime, time

@task(name='query_database')
def query_database():
    curr_time = str(datetime.now().time().strftime("%H:%M"))
    notification_query = Notification.objects.filter(time__contains=curr_time)
    for notification in notification_query:
        send_notification(notification)

