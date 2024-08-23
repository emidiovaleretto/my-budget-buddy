from django.urls import path
from . import views


urlpatterns = [
    path('new_amount/', views.new_amount, name='new_amount'),
    path('invoice/', views.invoice, name='invoice'),
    path('export_pdf/', views.export, name='export'),
]
