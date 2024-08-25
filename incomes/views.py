from datetime import date

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from django.contrib.messages import constants

from banking.models.Banks import Bank
from banking.models.Categories import Category
from .models.Incomes import Income



def new_income(request):
    if request.method == "GET":
        banks = Bank.objects.all()
        categories = Category.objects.all()
        current_date = date.today()

        context = {
            'banks': banks,
            'categories': categories,
            'current_date': current_date,
        }
        return render(request, 'incomes/add_income.html', context=context)

    amount = request.POST.get('amount')
    category = request.POST.get('category-name')
    description = request.POST.get('description')
    date_entry = request.POST.get('date')
    bank = request.POST.get('bank')
    type_of_entry = request.POST.get('type')

    try:
        new_entry = Income(
            amount=amount,
            category_id=category,
            description=description,
            date=date_entry,
            bank_id=bank,
            type_of_entry=type_of_entry
        )
        new_entry.save()

        bank = Bank.objects.get(id=bank)

        if type_of_entry == 'IN':
            bank.balance += int(amount)
        else:
            bank.balance -= int(amount)

        bank.save()
        messages.add_message(
            request,
            constants.SUCCESS,
            'Entry added successfully'
        )

        return redirect(reverse('home'))

    except Exception:
        messages.add_message(
            request,
            constants.ERROR,
            'An error occurred while adding entry'
        )
        return redirect(reverse('new_income'))
