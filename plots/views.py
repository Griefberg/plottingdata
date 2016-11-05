from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the plots index.")


def home(request):
    return render(request, 'home.html', {})


# def contact(request):
#     return render(request, 'forms.html', {})
