from django.urls import path
from . import views


urlpatterns = [
    path('planning/', views.set_planning, name='planning'),
]
