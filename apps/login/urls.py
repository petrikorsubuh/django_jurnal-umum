from django.contrib import admin
from django.urls import path

from apps.login import views

urlpatterns = [
    path('', views.LoginView.as_view()),
    path('process', views.LoginProccessView.as_view(), name='process'),
    path('logout', views.LogOutView.as_view(), name='logout'),
]
