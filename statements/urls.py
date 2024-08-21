from django.urls import path
from . import views


urlpatterns = [
    path('new_amount/', views.new_amount, name='new_amount'),
    path('view_statement/', views.view_statement, name='view_statement'),
    path('export_pdf/', views.export, name='export'),
]
