from django.shortcuts import redirect, render

def homePage(request):
    return render(request,'home.html')