from django.shortcuts import render, redirect


#-----------Student Section--------------------
def studentDashboard(request):
    
    return render(request,'students/studentdashboard.html')

def addStudent(request):
    
    return render(request,'students/addstudent.html')

def editStudent(request):
    
    return render(request,'students/editstudent.html')

def studentList(request):
    
    return render(request,'students/studentlist.html')

def studentDetails(request):
    
    return render(request,'students/studentdetails.html')