from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def about(request):
    # do something...
    return render(request, 'about.html')


def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})
