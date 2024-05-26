from django.shortcuts import render, redirect

def signupPage(request):
    
    return render(request,'commons/signup.html')

def signinPage(request):
    
    return render(request,'commons/signin.html')

#-----------Admin Section--------------------

def adminDashboard(request):
    
    return render(request,'admin/admindashboard.html')
