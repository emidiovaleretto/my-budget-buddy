from django.db import models

ENTRIES_CHOICES = (
    ("IN", "Income"),
    ("EX", ("Expense"))
)

from .Entries import Entry