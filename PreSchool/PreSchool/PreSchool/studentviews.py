from django.shortcuts import render, redirect
from PreSchoolApp.models import *


#-----------Student Section--------------------
def studentDashboard(request):
    
    return render(request,'students/studentdashboard.html')

def addStudent(request):
    if request.method == 'POST':
        fullname= request.POST.get('fullname')
        username= request.POST.get('username')
        studentid= request.POST.get('studentid')
        email= request.POST.get('email')
        gender= request.POST.get('gender')
        dateofbirth= request.POST.get('dateofbirth')
        department= request.POST.get('department')
        religion= request.POST.get('religion')
        joiningdate= request.POST.get('joiningdate')
        mobile= request.POST.get('mobile')
        password= request.POST.get('password')
        confirmpassword= request.POST.get('confirmpassword')
        section= request.POST.get('section')
        studentImage= request.FILES.get('studentImage')
        
        fathername= request.POST.get('fathername')
        fatheroccupation= request.POST.get('fatheroccupation')
        fathermobile= request.POST.get('fathermobile')
        fatheremail= request.POST.get('fatheremail')
        
        mothername= request.POST.get('mothername')
        motheroccupation= request.POST.get('motheroccupation')
        mothermobile= request.POST.get('mothermobile')
        motheremail= request.POST.get('motheremail')
        
        presentaddress= request.POST.get('presentaddress')
        permanentaddress= request.POST.get('permanentaddress')
        
        current_user = request.user
        if password == confirmpassword:
            user = customeUser.objects.create_user(username=username, password=password)
            user.email = email
            user.UserType = '3'
            user.ProfilePic = studentImage
            
            studentData = StudentModel(
                FullName=fullname,
                Username=username,
                StudentID=studentid,
                Gender=gender,
                DateOB=dateofbirth,
                Department=department,
                Religion=religion,
                JoiningDate=joiningdate,
                Mobile=mobile,
                Password=password,
                Section=section,
                
                FatherName=fathername,
                FatherOccupation=fatheroccupation,
                FatherMobile=fathermobile,
                FatherEmail=fatheremail,
                
                MotherName=mothername,
                MotherOccupation=motheroccupation,
                MotherMobile=mothermobile,
                MotherEmail=motheremail,
                
                PresentAddress=presentaddress,
                PermanentAddress=permanentaddress,
                Added_by=current_user,
            )
            
            user.save()
            studentData.save()
            return redirect('studentList')            
    
    
    return render(request,'students/addstudent.html')

def editStudent(request):
    
    return render(request,'students/editstudent.html')

def studentList(request):
    studentinfo = StudentModel.objects.all()
    
    
    stddict = {
        'studentinfo':studentinfo
    }
    
    
    return render(request,'students/studentlist.html',stddict)

def studentDetails(request,myid):
    studentinfo = StudentModel.objects.get(id=myid)
    userdata=customeUser.objects.get(username=studentinfo.Username)
    
    stddict = {
        'studentinfo':studentinfo,
        'userdata':userdata,
    }
    
    return render(request,'students/studentdetails.html',stddict)

def deleteStudent(request,myid):
    deletedata = StudentModel.objects.get(id=myid)
    customuser = deletedata.Username
    print("MY data: ",customuser)
    userdata=customeUser.objects.get(username=customuser)
    deletedata.delete()
    userdata.delete()
    
    return redirect('studentList')