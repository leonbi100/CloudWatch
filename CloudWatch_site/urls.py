from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from CloudWatch_site import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('notifications/', include([
    	path('', views.NotificationList.as_view(), name='notifications'),
	    path('create/', views.NotificationCreate.as_view(), name='notifications_create'),
	    path('<int:pk>/', include([
	    	path('update/', views.NotificationUpdate.as_view(), name='notifications_update'),
	    	path('delete/', views.NotificationDelete.as_view(), name='notifications_delete'),
	    ]))
	]))
]