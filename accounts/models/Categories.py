from django.utils.safestring import mark_safe
from accounts.models import *


class Category(models.Model):
    name = models.CharField(max_length=50)
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
