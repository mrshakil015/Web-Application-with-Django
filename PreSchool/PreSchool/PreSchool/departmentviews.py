from django.shortcuts import render, redirect


#-----------Depeartment Section--------------------

def addDepartment(request):
    
    return render(request,'department/adddepartment.html')

def editDepartment(request):
    
    return render(request,'department/editdepartment.html')

def departmentList(request):
    
    return render(request,'department/departmentlist.html')

