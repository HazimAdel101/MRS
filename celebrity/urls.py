from django.urls import path
from . import views


urlpatterns = [
    path('', views.celebrity, name='celebrity')
]
