from statements.models import *
from accounts.models.Categories import Category
from accounts.models.Accounts import Account


class Entry(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    type_of_entry = models.CharField(choices=ENTRIES_CHOICES, max_length=2)

    def __str__(self):
        return self.description
    
