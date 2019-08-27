from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from . import views

@periodic_task(
    run_every=(crontab(minute=18, hour=1)),
    name="send_notification",
    ignore_result=True
)
def send_notification():
	print('tried')
	views.weather()