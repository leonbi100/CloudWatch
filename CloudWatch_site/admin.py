from django.apps import apps
from django.contrib import admin
from .models import Notification

admin.site.register(Notification)
