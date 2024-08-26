from django.urls import reverse
from django.shortcuts import render, redirect
from banking.models.Categories import Category
from django.contrib import messages

from django.contrib.messages import constants


def set_up(request):
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
