from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.messages import constants

from banking.models.Categories import Category


def update_budget(request):
    if request.method == 'POST':

        for key, value in request.POST.items():
            if key.startswith('budget_'):
                category_id = key.split('_')[1]
                try:
                    category = Category.objects.get(id=category_id)
                    category.budget = value
                    category.save()
                    messages.add_message(
                        request,
                        constants.SUCCESS,
                        'Budget updated successfully.'
                    )
                except Category.DoesNotExist:
                    messages.add_message(
                        request,
                        constants.ERROR,
                        'An error occurred while updating the budget. Please try again.'
                    )
                    return redirect(reverse('home'))

    return redirect(reverse('home'))
