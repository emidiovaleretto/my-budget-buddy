from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('manage/', views.manage, name='manage'),
    path('add_account/', views.add_account, name='add_account'),
]
