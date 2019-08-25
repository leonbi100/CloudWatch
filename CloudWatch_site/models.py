from django.db import models
from users.models import CustomUser

class Notification(models.Model):
	is_set = models.BooleanField(default=False)
	time = models.DateTimeField(null=True, blank=True)
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)