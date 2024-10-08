from datetime import datetime
from django.utils.safestring import mark_safe

from banking.models import *
from django.db.models import Sum


class Category(models.Model):
    name = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_essential = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_essential_status(self):
        if self.is_essential:
            return mark_safe('<span class="badge-success">Yes</span>')
        return mark_safe('<span class="badge-danger">No</span>')

    def get_total_expenses(self):
        from incomes.models.Incomes import Income

        incomes = Income.objects.filter(category__id=self.id).filter(
            date__month=datetime.now()
            .month).exclude(
                type_of_entry__icontains=['in', 'fix']
        ).aggregate(Sum('amount'))
        return incomes['amount__sum'] if incomes['amount__sum'] else 0

    def get_percentage_per_category(self):
        try:
            return (self.get_total_expenses() * 100) / self.budget
        except Exception:
            return 0
