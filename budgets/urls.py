from django.urls import path
from . import views


urlpatterns = [
    path('new_budget/', views.new_budget, name='new_budget'),
]
