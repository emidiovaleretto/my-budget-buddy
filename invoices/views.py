import os
from io import BytesIO
from datetime import date, datetime

from django.conf import settings
from django.http import FileResponse

from django.shortcuts import render
from django.template.loader import render_to_string

from weasyprint import HTML

from accounts.models.Accounts import Account
from accounts.models.Categories import Category
from incomes.models.Incomes import Income


def invoice(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    entries = Income.objects.filter(date__month=datetime.now().month)

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
    entries = Income.objects.filter(date__month=datetime.now().month)
    accounts = Account.objects.all()
    categories = Category.objects.all()

    template_path = os.path.join(
        settings.BASE_DIR,
        'templates/partials/invoice.html'
    )
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
