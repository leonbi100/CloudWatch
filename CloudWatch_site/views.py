from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, View, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification

class NotificationView(View , LoginRequiredMixin):
    model = Notification

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NotificationList(NotificationView, ListView, LoginRequiredMixin):
    context_object_name = 'notification_list' 

    def get_context_data(self, **kwargs):
            context = super(NotificationList, self).get_context_data(**kwargs)
            return context

class NotificationCreate(NotificationView, CreateView, LoginRequiredMixin):
    fields = ('name', 'is_set', 'time') 

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('notifications')

class NotificationUpdate(NotificationView, UpdateView, LoginRequiredMixin):
    fields = ('name', 'is_set', 'time') 
    template_name_suffix = '_form'

    def get_success_url(self, **kwargs):
        return reverse_lazy('notifications')

class NotificationDelete(DeleteView, NotificationView, LoginRequiredMixin):
    model = Notification

    def get_success_url(self, **kwargs):
        return reverse_lazy('notifications')

