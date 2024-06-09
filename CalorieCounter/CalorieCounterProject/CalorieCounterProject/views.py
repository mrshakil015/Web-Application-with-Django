from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from CalorieCounterApp.models import *


def signupPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        confpassword=request.POST.get('confpassword')
        
        if psw == confpassword:
            user = CustomeUserModel.objects.create_user(
                username=username,
                password = psw,
                email = email,
            )
            user.save()
            return redirect('signinPage')
    
    return render(request,'signup.html')

def signinPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        psw=request.POST.get('psw')
        
        user = authenticate(username=username, password = psw)
        if user:
            login(request,user)
            return redirect('dashboardPage')
    
    return render(request,'signin.html')

@login_required
def dashboardPage(request):
    current_user = request.user
    
    calorisdata = CaloriesModel.objects.filter(MyUser=current_user)
    context = {
        'calorisdata':calorisdata,
    }
    
    
    return render(request,'dashboard.html',context)
    
def logoutPage(request):
    logout(request)
    return redirect('signinPage')

@login_required
def addPersonalInfo(request):
    current_user = request.user
    
    userData = CustomeUserModel.objects.get(username = current_user)
    context = {
        'userData':userData,
    }
    
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        
        if gender == 'Male':
            BMRCal = 66.47 + (13.75 * float(weight)) + (5.003 * float(height)) - (6.755 * int(age))
        else:
            BMRCal = 655.1 + (9.563 * float(weight)) + (1.850 * float(height)) - (4.676 * int(age))
        
        userData.Name = fullname
        userData.Age = age
        userData.Gender = gender
        userData.Height = height
        userData.Weight = weight
        userData.BMRCal = BMRCal
        userData.save()
        return redirect('dashboardPage')
    
    return render(request,'addpersonalinfo.html',context)

def calroyCounter(request):
    current_user = request.user
    BMRCal = request.user.BMRCal
    if request.method == 'POST':
        itemname = request.POST.get('itemname')
        itemcalories = request.POST.get('itemcalories')
        
        CaloriesConsumed = float(BMRCal) * float(itemcalories)
        
        caloriesdata = CaloriesModel.objects.create(
            ItemName = itemname,
            ItemCalories = itemcalories,
            CaloriesConsumed = CaloriesConsumed,
            MyUser=current_user,
        )
        caloriesdata.save()
        return redirect('dashboardPage')
        
    return render(request,'calorycounter.html')