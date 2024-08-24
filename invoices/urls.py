from django.urls import path
from . import views


urlpatterns = [
    path('invoice/', views.invoice, name='invoice'),
    path('export_pdf/', views.export, name='export'),
]
