from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_income, name='new_income'),
]
