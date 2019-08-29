from django.db import models
from users.models import CustomUser
from timezone_field import TimeZoneField
import arrow
from datetime import datetime, date, timedelta


class Notification(models.Model):
    name = models.CharField(max_length=255, null=True)
    is_set = models.BooleanField(default=False)
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    time_zone = TimeZoneField(default='UTC')
    date_created = models.DateTimeField(auto_now_add=True)
    task_id = models.CharField(max_length=50, blank=True, editable=False)

    def __str__(self):
        return '%s' % self.name

    # def schedule_notification(self):
    #     # Convert time to datetime object and set for tomorrow
    #     datetime_str = '{} {}'.format(date.today(), self.time)
    #     date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S') + timedelta(days=1)

    #     notification_time = arrow.get(date_time_obj, self.time_zone.zone)
    #     from .tasks import send_notification
    #     result = send_notification(self.pk)
    #     return result.options['redis_message_id']

    # """Custom save method which schedules notification"""
    # def save(self, *args, **kwargs):

    #     # Check if scheduled before
    #     if self.task_id:
    #         self.cancel_task()
    #     # Save new task 
    #     super(Notification, self).save(*args, **kwargs)
    #     self.task_id = self.schedule_notification()
    #     super(Appointment, self).save(*args, **kwargs)

    # def cancel_task(self):
    #     redis_client = redis.Redis(host='localhost', port=6379, db=0)
    #     redis_client.hdel("dramatiq:default.DQ.msgs", self.task_id)