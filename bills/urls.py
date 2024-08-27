from django.urls import path
from . import views

urlpatterns = [
    path('set_up/', views.set_up, name="set_up"),
    path('view_bills/', views.view_bills, name="view_bills"),
]
