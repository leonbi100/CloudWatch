from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, View, CreateView, DeleteView
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification
from twilio.rest import Client
from darksky import forecast
from django_CloudWatch.local_settings import account_sid, auth_token, Dark_Sky_Key
from datetime import date, timedelta
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")

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

def weather():
    latitude, longitude = get_lat_long('231 Gennessee St. San Francisco') 
    message = get_forecast((latitude, longitude))
    send_sms(message)


def get_lat_long(address):
    location = geolocator.geocode(address)
    print(location.address)
    print((location.latitude, location.longitude))
    return location.latitude, location.longitude

def get_forecast(location):
    weather = forecast(Dark_Sky_Key, location[0], location[1])
    return "Weekly Summary: {} \n Today's Wind Speed: {}".format(weather.daily.summary, weather.windSpeed)
    # print(weather.temperatureMax)
    # with forecast(Dark_Sky_Key, *PLACE) as place:
    #     weekly_summary = place.daily.summary
    #     print(weekly_summary)
    #     print(place.)
        # print("temp max: {}".format(place.daily.temperatureMax))

        # message = "Weekly Summary: {} \n Today's Summary: {} \n Temp Range: {} - {}".format(weekly_summary, day.summary, day.temperatureMin, day.temperatureMax)
    # return message

def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body = message,
                     from_='+12405585791',
                     to='+12403288453'
                 )
    print(message.sid)



