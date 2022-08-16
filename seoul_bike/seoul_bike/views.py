from django.shortcuts import render
from . import visual
from .models import *
from django.http import HttpResponse
from . import visual

def index(request):
    contexts = dict()

    contexts['yearUsage'] = visual.year_usage()
    contexts['rain_usage'] = visual.rain_usage()
    contexts['countStationId'] = visual.countStationId()
    contexts['topStation_id'] = visual.topStation_id()
    return render(request, 'index.html', contexts)



def time1(request):
    contexts = dict()
    contexts['timeusage'] = visual.timeusage()
    return render(request, 'time1.html', contexts)

def time21(request):
    contexts = dict()
    contexts['lifeusage'] = visual.lifeusage()
    return render(request, 'time21.html', contexts)

def time22(request):
    contexts = dict()
    contexts['subusage'] = visual.subusage()
    return render(request, 'time22.html', contexts)

def time23(request):
    contexts = dict()
    contexts['bususage'] = visual.bususage()
    return render(request, 'time23.html', contexts)

def facilities1(request):
    contexts = dict()
    return render(request, 'facilities1.html', contexts)

def facilities2(request):
    contexts = dict()
    return render(request, 'facilities2.html', contexts)

def facilities3(request):
    contexts = dict()
    return render(request, 'facilities3.html', contexts)
