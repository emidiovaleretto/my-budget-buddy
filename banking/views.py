from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.http import JsonResponse
from django.template.loader import render_to_string

from banking.models import Bank
from banking.models import Category
from incomes.models.Incomes import Income

from bills.models.Bills import Payable
from .utils import calculate_total


@login_required(login_url='accounts/login/')
def home(request):
    banks = Bank.objects.all()
    categories = Category.objects.all()
    bills = Payable.objects.all()

    incomes = Income.objects.exclude(
        type_of_entry__icontains='ex'
    ).exclude(
        type_of_entry__icontains='fix'
    )

    expenses = Income.objects.exclude(
        type_of_entry__icontains='in'
    )

    total_balance = calculate_total(banks, 'balance')
    total_income = calculate_total(incomes, 'amount')
    total_expenses = calculate_total(expenses, 'amount')

    remaining_balance = total_income - total_expenses

    context = {
        'banks': banks,
        'categories': categories,
        'bills': bills,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'total_balance': total_balance,
        'remaining_balance': remaining_balance
    }
    return render(request, 'banks/home.html', context=context)


@login_required(login_url='accounts/login/')
def manage(request):
    banks = Bank.objects.all()
    categories = Category.objects.all()
    total = sum([bank.balance for bank in banks])
    
    paginator = Paginator(categories, 4)
    page_number = request.GET.get('page')
    per_page = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('partials/category_table.html', {'per_page': per_page})
        pagination_html = render_to_string('partials/pagination.html', {'per_page': per_page})
        return JsonResponse({'html': html, 'pagination_html': pagination_html})


    context = {
        'banks': banks,
        'categories': categories,
        'per_page': per_page,
        'total': total
    }

    return render(request, 'banks/manage.html', context=context)


@login_required(login_url='accounts/login/')
def add_account(request):
    label = request.POST.get('label_account')
    bank = request.POST.get('bank')
    account_type = request.POST.get('account_type')
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
        account = Bank(
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


@login_required(login_url='accounts/login/')
def remove_account(request, account_id):
    account = get_object_or_404(Bank, id=account_id)
    account.delete()

    messages.add_message(
        request,
        constants.SUCCESS,
        f'Account {account.label.upper()} successfully deleted.'
    )
    return redirect(reverse('manage'))


@login_required(login_url='accounts/login/')
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

            if Category.objects.filter(name=category_name).exists():
                messages.add_message(
                    request,
                    constants.ERROR,
                    'This category has been registered before.'
                )
                return redirect(reverse('manage'))

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

    return render(request, 'banks/manage.html')


@login_required(login_url='accounts/login/')
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.is_essential = not category.is_essential
    category.save()

    return redirect(reverse('manage'))
