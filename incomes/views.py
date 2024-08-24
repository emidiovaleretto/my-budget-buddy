from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.messages import constants

from accounts.models.Accounts import Account
from accounts.models.Categories import Category
from .models.Incomes import Income



def new_income(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()
        current_date = date.today()

        context = {
            'accounts': accounts,
            'categories': categories,
            'current_date': current_date,
        }
        return render(request, 'incomes/add_income.html', context=context)

    amount = request.POST.get('amount')
    category = request.POST.get('category-name')
    description = request.POST.get('description')
    date_entry = request.POST.get('date')
    account = request.POST.get('account')
    type_of_entry = request.POST.get('type')

    try:
        new_entry = Income(
            amount=amount,
            category_id=category,
            description=description,
            date=date_entry,
            account_id=account,
            type_of_entry=type_of_entry
        )
        new_entry.save()

        account = Account.objects.get(id=account)

        if type_of_entry == 'IN':
            account.balance += int(amount)
        else:
            account.balance -= int(amount)

        account.save()
        messages.add_message(
            request,
            constants.SUCCESS,
            'Entry added successfully'
        )

        return redirect(reverse('home'))

    except Exception as e:
        print(f'An error occurred while adding entry: {e}')
        messages.add_message(
            request,
            constants.ERROR,
            'An error occurred while adding entry'
        )
        return redirect(reverse('new_income'))
