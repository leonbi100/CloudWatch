from django.db import models
from users.models import CustomUser

class Notification(models.Model):
    name = models.CharField(max_length=255, null=True)
    is_set = models.BooleanField(default=False)
    time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.name