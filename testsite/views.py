from django.http import HttpResponse 
from django.shortcuts import render
from.models import TestData

def testsite(request):
    data = TestData.objects.all()
    return render(request, 'testsite/testsite.html', {'testsite' : data})

def home(request):
    return HttpResponse("Home page")

def detail(request, id):
    data = testsite.objects.get(pk=id)
    return render(request, 'testsite/detail.html', {'testsite': data})

