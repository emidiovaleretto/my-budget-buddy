from django.db import models
from banking.models.Categories import Category


class Payable(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    logo = models.ImageField(upload_to="logos/", null=True, blank=True)

    def __str__(self):
        return self.title
    

class Paid(models.Model):
    bill = models.ForeignKey(Payable, on_delete=models.CASCADE)
    paid_date = models.DateField(auto_now=False, auto_now_add=False)
