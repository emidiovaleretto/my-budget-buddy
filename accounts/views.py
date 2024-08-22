from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.messages import constants
from accounts.models import Account
from accounts.models import Category

from .utils import calculate_total


def home(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    total_balance = calculate_total(accounts, 'balance')
    context = {
        'accounts': accounts,
        'categories': categories,
        'total_balance': total_balance
    }
    return render(request, 'accounts/home.html', context=context)


def manage(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    total = sum([account.balance for account in accounts])
    context = {
        'accounts': accounts,
        'categories': categories,
        'total': total
    }
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


def remove_account(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    account.delete()

    messages.add_message(
        request,
        constants.SUCCESS,
        f'Account {account.label.upper()} successfully deleted.'
    )
    return redirect(reverse('manage'))


def add_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category-name')
        is_essential = bool(request.POST.get('is-essential'))
        other_category = request.POST.get('other-category')

        if other_category:
            category_name = other_category

        try:
            category = Category(
                name=category_name,
                is_essential=is_essential
            )
            category.save()
            messages.add_message(
                request,
                constants.SUCCESS,
                'Category successfully added.'
            )
            return redirect(reverse('manage'))

        except Exception:
            messages.add_message(
                request,
                constants.ERROR,
                'An error occurred while adding the category. Please try again.'
            )
            return redirect(reverse('manage'))

    return render(request, 'accounts/manage.html')


def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.is_essential = not category.is_essential
    category.save()

    return redirect(reverse('manage'))


def remove_category(request, category_id):
    pass
