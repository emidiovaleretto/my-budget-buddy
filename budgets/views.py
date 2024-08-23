from django.shortcuts import render
from accounts.models.Categories import Category


def new_budget(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'budgets/new_budget.html', context=context)
