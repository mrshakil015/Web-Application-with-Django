from django.shortcuts import render, redirect
from myApp.models import *

def home(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'home.html',datadict)
def about(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'about.html',datadict)
def resume(request):
    aboutdata=AboutModel.objects.get()
    educationdata=EducationModel.objects.all()
    datadict={
        'aboutdata': aboutdata,
        'educationdata': educationdata,
    }
    return render(request, 'resume.html',datadict)
def contact(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'contact.html',datadict)
def sidebar(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'sidebar.html',datadict)

def edithome(request):
    homedata=AboutModel.objects.get()
    homedict={
        'homedata': homedata 
    }
    return render(request, 'edithome.html',homedict)
def editabout(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'editabout.html',datadict)
def editeducation(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'editeducation.html',datadict)
def editwork(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'editwork.html',datadict)

def editcontact(request):
    aboutdata=AboutModel.objects.get()
    datadict={
        'aboutdata': aboutdata 
    }
    return render(request, 'editcontact.html',datadict)
