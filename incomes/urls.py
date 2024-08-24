from django.urls import path
from . import views

urlpatterns = [
    path('new_income/', views.new_income, name='new_income'),
]
