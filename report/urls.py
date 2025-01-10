# urls.py
from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('overview/', views.report_overview, name='overview'),
]