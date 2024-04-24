from django.shortcuts import render, redirect
from jobPortalApp.models import *
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        display_name=request.POST.get('displayname')
        user_name=request.POST.get('username')
        father_name=request.POST.get('fname')
        mother_name=request.POST.get('mname')
        address=request.POST.get('address')
        bloodgroup=request.POST.get('bloodgroup')
        profileimg=request.FILES.get('profileimg')
        email_address=request.POST.get('email')
        pass_word=request.POST.get('password')
        confirm_Password=request.POST.get('confirmPassword')
        userType=request.POST.get('userType')
        
        if pass_word==confirm_Password:
            user=Custom_User.objects.create_user(username=user_name, password=pass_word)
            user.displayname=display_name
            user.email=email_address
            user.user_type=userType
            user.fathername=father_name
            user.mothername=mother_name
            user.address=address
            user.blood_group=bloodgroup
            user.profileimg=profileimg
            
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        
        user=authenticate(username=user_name, password=pass_word)
        
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
        
    return render(request,'signin.html')

def logoutPage(request):
    logout(request)
    
    return redirect('signin')

@login_required
def dashboard(request):
    jobdata=AddJobModel.objects.filter(RecruiterName=request.user.username)
    
    jobdict={
        'jobdata':jobdata
    }
    return render(request,'dashboard.html',jobdict)

@login_required
def addjob(request):
    if request.method=='POST':
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        companyAddress=request.POST.get('companyAddress')
        companyDescription=request.POST.get('companyDescription')
        jobDescription=request.POST.get('jobDescription')
        salary=request.POST.get('salary')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        
        addJobdata= AddJobModel(
            JobTitle=jobTitle,
            CompanyName=companyName,
            CompanyDescription=companyAddress,
            JobDescription=companyDescription,
            Qualification=jobDescription,
            Salary=salary,
            Designation=designation,
            Deadline=deadline,
            Experience=experience,
            RecruiterName=request.user.username
        )
        addJobdata.save()
        return redirect('dashboard')
    
    return render(request,'Recruiter/addjob.html')

@login_required
def editjob(request,myid):
    jobdata=AddJobModel.objects.get(id=myid)
    jobdict={
        'jobdata':jobdata
    }  
    return render(request,'editjob.html',jobdict)

@login_required
def updatejob(request):
    if request.method=='POST':
        jobid=request.POST.get('jobid')
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        companyAddress=request.POST.get('companyAddress')
        companyDescription=request.POST.get('companyDescription')
        jobDescription=request.POST.get('jobDescription')
        salary=request.POST.get('salary')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        
        addJobdata= AddJobModel(
            id=jobid,
            JobTitle=jobTitle,
            CompanyName=companyName,
            CompanyDescription=companyAddress,
            JobDescription=companyDescription,
            Qualification=jobDescription,
            Salary=salary,
            Designation=designation,
            Deadline=deadline,
            Experience=experience,
            RecruiterName=request.user.username
        )
        addJobdata.save()
        return redirect('dashboard')
    
@login_required
def viewjob(request):
    
    jobdata=AddJobModel.objects.all()
    jobdict={
        'jobdata':jobdata
    }
    
    return render(request,'Seeker/viewjob.html',jobdict)

@login_required
def deletejob(request,myid):
    jobdata=AddJobModel.objects.get(id=myid)
    
    jobdata.delete()
    return redirect('dashboard')

@login_required
def profile(request):
    
    return render(request,'profile.html')
def appliedJob(request):
    
    return render(request,'Seeker/appliedJob.html')
