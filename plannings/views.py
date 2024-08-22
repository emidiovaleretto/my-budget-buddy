from django.shortcuts import render
from accounts.models.Categories import Category


def set_budget(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'plannings/set_planning.html', context=context)
