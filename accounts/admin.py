from django.contrib import admin
from .models.Categories import Category
from .models.Accounts import Account


admin.site.register(Category)
admin.site.register(Account)
