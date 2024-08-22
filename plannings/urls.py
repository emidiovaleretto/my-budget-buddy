from django.urls import path
from . import views


urlpatterns = [
    path('budget/', views.set_budget, name='budget'),
]
