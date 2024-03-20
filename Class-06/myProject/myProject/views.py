from django.shortcuts import render
from myApp.models import *


def studentpage(request):
    student=studentModel.objects.all()
    mydir={
        'std':student
    }
    return render(request, 'studentpage.html',mydir)

def teacherpage(request):
    message = 'Hello, teacher!'
    return render(request, 'teacherpage.html', {'message': message})

def managementpage(request):
    management=managementModel.objects.all()
    
    mydir={
        'std':management
    }
    return render(request, 'managementpage.html',mydir)

def staffpage(request):
    staff=staffModel.objects.all()
    
    mydir={
        'std':staff
    }
    return render(request, 'staffpage.html',mydir)

def librarypage(request):
    library=libraryModel.objects.all()
    
    libdic={
        'std':library
    }
    return render(request, 'librarypage.html', libdic)

