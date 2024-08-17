from django.contrib.auth.models import User
from accounts.models import *


class Account(models.Model):
    label = models.CharField(max_length=50)
    bank = models.CharField(max_length=4, choices=BANK_CHOICES)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPE_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label
