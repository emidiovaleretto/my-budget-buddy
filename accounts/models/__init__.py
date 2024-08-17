from django.db import models


BANK_CHOICES = (
    ("AIB", "Allied Irish Banks"),
    ("BOI", "Bank of Ireland"),
    ("PTSB", "Permanent TSB"),
    ("ANP", "An Post Money"),
    ("REV", "Revolut"),
    ("N26", "N26"),
    ("CU", "Credit Union"),
    ("OTH", "Other")
)

ACCOUNT_TYPE_CHOICES = (
    ("PA", "Personal Account"),
    ("BE", "Business Entity")
)


from .Categories import Category
from .Accounts import Account
