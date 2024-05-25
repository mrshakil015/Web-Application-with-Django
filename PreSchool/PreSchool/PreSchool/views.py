from django.shortcuts import render, redirect

def signupPage(request):
    
    return render(request,'commons/signup.html')

def signinPage(request):
    
    return render(request,'commons/signin.html')

def teacherDashboard(request):
    
    return render(request,'teachers/teacherdashboard.html')

def studentDashboard(request):
    
    return render(request,'students/studentdashboard.html')

def addStudent(request):
    
    return render(request,'students/addstudent.html')

def editStudent(request):
    
    return render(request,'students/editstudent.html')

def studentList(request):
    
    return render(request,'students/studentlist.html')

#-----------Admin Section--------------------

def adminDashboard(request):
    
    return render(request,'admin/admindashboard.html')

def componentPage(request):
    
    return render(request,'commons/components.html')