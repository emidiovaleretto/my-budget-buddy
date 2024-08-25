from django.contrib import admin
from .models.Categories import Category
from .models.Banks import Bank


admin.site.register(Category)
admin.site.register(Bank)
