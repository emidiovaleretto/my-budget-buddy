from django.contrib import admin
from .models.Bills import Payable, Paid

admin.site.register(Payable)
admin.site.register(Paid)
