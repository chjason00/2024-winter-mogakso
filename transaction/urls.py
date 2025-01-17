# urls.py
from django.urls import path
from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.transaction_list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]