from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('log',LoginView.as_view(),name='log'),
    path('reg',RegView.as_view(),name='reg'),
    path('lout',LogoutView.as_view(),name='lout')
]