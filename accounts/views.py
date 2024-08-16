from django.shortcuts import render


def home(request):
    return render(request, 'accounts/home.html')


def manage(request):
    return render(request, 'accounts/manage.html')
