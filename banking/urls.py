from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', views.manage, name='manage'),
    path('banking/accounts/', views.add_account, name='add_account'),
    path(
        'banking/accounts/<int:account_id>/',
        views.remove_account,
        name='remove_account'),
    path('banking/categories/', views.add_category, name='add_category'),
    path('banking/categories//<int:category_id>/',
         views.update_category, 
         name='update_category'
         ),
]
