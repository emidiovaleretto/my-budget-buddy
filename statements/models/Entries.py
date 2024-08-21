from django.db import models
from django.utils.safestring import mark_safe

from statements.models import ENTRIES_CHOICES
from accounts.models.Categories import Category
from accounts.models.Accounts import Account


class Entry(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type_of_entry = models.CharField(choices=ENTRIES_CHOICES, max_length=2)

    def __str__(self):
        return self.description

    @property
    def get_type_of_entry(self):
        if self.type_of_entry == "EX":
            return mark_safe('<span class="badge-danger">Expense</span>')
        return mark_safe('<span class="badge-success">Income</span>')
