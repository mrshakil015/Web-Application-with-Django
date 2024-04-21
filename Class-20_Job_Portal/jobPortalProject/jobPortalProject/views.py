from django.shortcuts import render, redirect

def signup(request):
    if request.method=='POST':
        usertype=request.POST.get('usertype')
        username=request.POST.get('username')
        
        
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
