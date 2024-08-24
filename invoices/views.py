import os
from io import BytesIO
from datetime import date, datetime

from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.messages import constants
from django.conf import settings
from django.http import FileResponse

from django.template.loader import render_to_string

from weasyprint import HTML

from accounts.models.Accounts import Account
from accounts.models.Categories import Category
from .models.Invoices import Invoice



def new_amount(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()
        current_date = date.today()

        context = {
            'accounts': accounts,
            'categories': categories,
            'current_date': current_date,
        }
        return render(request, 'invoices/add_entries.html', context=context)

    amount = request.POST.get('amount')
    category = request.POST.get('category-name')
    description = request.POST.get('description')
    date_entry = request.POST.get('date')
    account = request.POST.get('account')
    type_of_entry = request.POST.get('type')

    try:
        new_entry = Invoice(
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
        return redirect(reverse('new_amount'))


def invoice(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    entries = Invoice.objects.filter(date__month=datetime.now().month)

    account_form = request.GET.get('account')
    category_form = request.GET.get('category')

    if account_form:
        entries = entries.filter(account__id=account_form)
    if category_form:
        entries = entries.filter(category__id=category_form)

    context = {
        'accounts': accounts,
        'categories': categories,
        'entries': entries,
    }

    return render(request, 'invoices/invoice.html', context=context)


def export(request):
    entries = Invoice.objects.filter(date__month=datetime.now().month)
    accounts = Account.objects.all()
    categories = Category.objects.all()

    template_path = os.path.join(settings.BASE_DIR, 'templates/partials/invoice.html')
    output_path = BytesIO()

    context = {
        'entries': entries,
        'accounts': accounts,
        'categories': categories
    }

    template_render = render_to_string(
        template_path,
        context
    )

    HTML(string=template_render).write_pdf(output_path)
    output_path.seek(0)

    return FileResponse(
        output_path,
        filename=f"statement-{date.today().strftime('%d-%m-%Y')}.pdf"
    )