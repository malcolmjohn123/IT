
from django.contrib import admin
from django.urls import path, include
from .views import Homepage, Login
app_name = 'visualization'

urlpatterns = [
    path('', Homepage.as_view(), name = 'homepage'),
    path('login/', Login.as_view(), name = 'login')
]
