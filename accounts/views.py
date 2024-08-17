from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.messages import constants
from accounts.models import Account


def home(request):
    return render(request, 'accounts/home.html')


def manage(request):
    accounts = Account.objects.all()
    total = sum([account.balance for account in accounts])
    context = {'accounts': accounts, 'total': total}
    return render(request, 'accounts/manage.html', context=context)


def add_account(request):
    if request.method == 'GET':
        return render(request, 'accounts/add_account.html')
    
    label = request.POST.get('label_account')
    bank = request.POST.get('bank')
    account_type = request.POST.get('bank_type')
    balance = request.POST.get('balance')
    logo = request.FILES.get('bank_logo')

    if not label or not balance:
        print(f"Label: {label}, Balance: {balance}")
        messages.add_message(
            request,
            constants.ERROR,
            'Please fill in all required fields.'
        )
        return redirect(reverse('manage'))
    
    try:
        account = Account(
            label=label,
            bank=bank,
            account_type=account_type,
            balance=balance,
            logo=logo)
        
        account.save()
        messages.add_message(
            request,
            constants.SUCCESS,
            'Your account was successfully saved.'
        )
        return redirect(reverse('manage'))

    except Exception:
        messages.add_message(
            request, 
            constants.ERROR,
            'An error occurred while saving your business. Please try again.'
        )
        return redirect(reverse('manage'))
