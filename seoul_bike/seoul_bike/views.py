from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def time1(request):
    return render(request, 'time1.html')

def time2(request):
    return render(request, 'time2.html')

def facilities1(request):
    return render(request, 'facilities1.html')

def facilities2(request):
    return render(request, 'facilities2.html')

def facilities3(request):
    return render(request, 'facilities3.html')
