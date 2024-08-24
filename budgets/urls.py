from django.urls import path
from . import views


urlpatterns = [
    path('update_budget/', views.update_budget, name='update_budget'),
]
