from django.shortcuts import redirect, render
from portfolio.models import *

def homePage(request):
    info=infoModel.objects.get(id=1)
    infodict={
        'info':info
    }
    return render(request,'home.html',infodict)

def aboutPage(request):
    info=infoModel.objects.get(id=1)
    infodict={
        'info':info
    }
    return render(request,'about.html',infodict)

def educationPage(request):
    info=infoModel.objects.get(id=1)
    infodict={
        'info':info
    }
    return render(request,'education.html',infodict)