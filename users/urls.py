from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', views.UserUpdate.as_view(), name='profile'),
]