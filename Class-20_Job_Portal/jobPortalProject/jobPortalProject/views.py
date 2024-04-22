from django.shortcuts import render, redirect
from jobPortalApp.models import *

def signup(request):
    if request.method=='POST':
        display_name=request.POST.get('displayname')
        user_name=request.POST.get('username')
        email_address=request.POST.get('email')
        pass_word=request.POST.get('password')
        confirm_Password=request.POST.get('confirmPassword')
        userType=request.POST.get('userType')
        
        if pass_word==confirm_Password:
            user=Custom_User.objects.create_user(username=user_name, password=pass_word)
            user.displayname=display_name
            user.email=email_address
            user.user_type=userType
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
