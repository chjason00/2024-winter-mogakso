# urls.py
from django.urls import path
from . import views

app_name = 'asset'

urlpatterns = [
    path('', views.overview, name='overview'),
]