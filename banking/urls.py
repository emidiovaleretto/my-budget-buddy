from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('manage/', views.manage, name='manage'),
    path('add_account/', views.add_account, name='add_account'),
    path(
        'remove_account/<int:account_id>/',
        views.remove_account,
        name='remove_account'),
    path('add_category/', views.add_category, name='add_category'),
    path('update_category/<int:category_id>/',
         views.update_category, 
         name='update_category'
         ),
]
