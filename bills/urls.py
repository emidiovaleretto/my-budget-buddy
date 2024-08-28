from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_up, name="set_up"),
    path('overview/', views.view_bill, name="view_bill"),
]
