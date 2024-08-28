from datetime import datetime
from django.urls import reverse
from django.shortcuts import render, redirect

from .models.Bills import Payable, Paid
from banking.models.Categories import Category
from django.contrib import messages

from django.contrib.messages import constants


def set_up(request):
    """
    This function is responsible for rendering the set up page for the bills.
    It also handles the POST request to save the bill in the database.
    """

    if request.method == "POST":
        title = request.POST.get("title")
        category = request.POST.get("category")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        due_date = request.POST.get("date")
        logo = request.FILES.get('logo')

        try:
            bill = Payable(
                title=title,
                category_id=category,
                description=description,
                amount=amount,
                due_date=due_date,
                logo=logo
            )

            bill.save()

            messages.add_message(
                request,
                constants.SUCCESS,
                'Your bill was registered successfully.'
            )

            return redirect(reverse("home"))

        except Exception:
            messages.add_message(
                request,
                constants.ERROR,
                'An error occurred while saving your business. Please try again.'
            )
            return redirect(reverse("set_up"))

    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request, "bills/set_up.html", context=context)


def view_bill(request):
    CURRENT_MONTH = datetime.now().month
    CURRENT_DAY = datetime.now().day

    payable_bills = Payable.objects.all()

    paid_bills = Paid.objects.filter(
        paid_date__month=CURRENT_MONTH).values('bill')

    overdue_bills = payable_bills.filter(
        due_date__day=CURRENT_DAY).exclude(id__in=paid_bills)

    next_due_date_bills = payable_bills.filter(
        due_date__day=CURRENT_DAY + 5).filter(due_date__day=CURRENT_DAY).exclude(id__in=paid_bills)

    remaining_bills = payable_bills.exclude(id__in=overdue_bills).exclude(
        id__in=paid_bills).exclude(id__in=next_due_date_bills)

    context = {
        'payable_bills': payable_bills,
        'paid_bills': paid_bills,
        'overdue_bills': overdue_bills,
        'next_due_date_bills': next_due_date_bills,
        'remaining_bills': remaining_bills
    }

    return render(request, 'bills/set_up.html', context=context)
