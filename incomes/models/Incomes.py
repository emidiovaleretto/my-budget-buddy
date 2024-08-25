from django.db import models
from django.utils.safestring import mark_safe

from incomes.models import INCOME_TYPE_CHOICES
from banking.models.Categories import Category
from banking.models.Banks import Bank


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    type_of_entry = models.CharField(choices=INCOME_TYPE_CHOICES, max_length=3)

    def __str__(self):
        return self.description

    @property
    def get_type_of_entry(self):
        if self.type_of_entry == "IN":
            return mark_safe('<span class="badge-success">Income</span>')
        elif self.type_of_entry == "EX":
            return mark_safe('<span class="badge-danger">Expense</span>')
        return mark_safe('<span class="badge-warning">Fixed Expense</span>')
