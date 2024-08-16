from django.shortcuts import render


def home(request):
    return render(request, 'profiles/home.html')


def manage(request):
    return render(request, 'profiles/manage.html')
