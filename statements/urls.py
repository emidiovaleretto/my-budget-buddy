from django.urls import path
from . import views


urlpatterns = [
    path('new_balance', views.new_balance, name='new_balance'),
]
