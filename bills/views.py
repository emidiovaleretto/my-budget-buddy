from django.shortcuts import render
from banking.models.Categories import Category


def set_up(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request, "bills/set_up.html", context=context)
