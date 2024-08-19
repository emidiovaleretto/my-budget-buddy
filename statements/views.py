from django.shortcuts import render

from accounts.models.Accounts import Account
from accounts.models.Categories import Category

from datetime import date


def new_balance(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()
        current_date = date.today()

        print(current_date)

        context = {
            'accounts': accounts,
            'categories': categories,
            'current_date': current_date,
        }

        return render(request, 'statements/add_entries.html', context=context)
