from django.shortcuts import redirect, render
from jobPortalApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PIL import Image
from django.contrib.auth.hashers import check_password

context = {
    'success_msg':'Successfully Created.',
    'username_msg':'Username Already Existed.',
    'imagesize_msg':'Image must be less than 1MB.',
    'imageresulation_msg':'Image resulation must be 500 x 500 px.',
}


def signupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        fullName=request.POST.get('fullName')
        email=request.POST.get('email')
        address=request.POST.get('address')
        password=request.POST.get('password')
        confpassword=request.POST.get('confpassword')
        profileImage=request.FILES.get('profileImage')
        userType=request.POST.get('userType')
        #---------- Image resulation----------
        imgre = Image.open(profileImage)
        width, height = imgre.size
        #-----------Image size -----------
        imagesize = profileImage.size
        recsize = 1024 * 1024
        #--------User exists---------------
        user_exist = Job_User.objects.filter(username=username).exists()
        if user_exist:
            messages.error(request,context['username_msg']) 
        elif imagesize > recsize:
            messages.warning(request,context['imagesize_msg'])
        elif width !=500 and height != 500:
            messages.warning(request,context['imageresulation_msg'])
        else:
            if password==confpassword:
                user = Job_User.objects.create_user(username=username, password=password)
                user.FullName=fullName
                user.email=email
                user.Address=address
                user.UserType=userType
                user.ProfileImage=profileImage 
                if userType=='Recuriter':
                    RecruiterProfileModel.objects.create(myUser=user)
                    BasicInfoModel.objects.create(myUser=user)
                    contactModel.objects.create(myUser=user)
                else:
                    SeekerProfileModel.objects.create(myUser=user)
                    BasicInfoModel.objects.create(myUser=user)
                    contactModel.objects.create(myUser=user)
                    EducationalModel.objects.create(myUser=user)
                    WorkExperinceModel.objects.create(myUser=user)
            
                user.save()
                messages.success(request,context['success_msg'])
                return redirect('signinPage')
            else:
                messages.warning(request,'Password and Confirm Password not matched.')
                return redirect('signupPage')
    return render(request,'signup.html')

def signinPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Username and Password not valid.')
            return redirect('signinPage')
    
    return render(request,'signin.html')

@login_required
def dashboard(request):
    
    return render(request,'dashboard.html')

@login_required
def profile(request):
    
    # profiledata=
    
  
    return render(request,'profile.html')

@login_required
def AddJob(request):
    if request.method=='POST':
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        companyAddress=request.POST.get('companyAddress')
        description=request.POST.get('description')
        salary=request.POST.get('salary')
        experiences=request.POST.get('experiences')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        
        current_user = request.user
        
        addjobdata = AddJobModel(
            JobTitle=jobTitle,
            CompanyName=companyName,
            CompanyAddress=companyAddress,
            Designation=designation,
            JobDescription=description,
            Salary=salary,
            Experience=experiences,
            Deadline=deadline,
            Created_by=current_user,
        )
        addjobdata.save()
        return redirect('JobList')
    
    return render(request,'Recuriter/addjob.html')

@login_required
def AppliedJob(request):
    
    return render(request,'Seeker/appliedjob.html')

@login_required
def JobList(request):
    current_user = request.user
    current_usertype= request.user.UserType
    
    if current_usertype == 'Recuriter':
        jobdata=AddJobModel.objects.filter(Created_by=current_user)
    else:
        jobdata=AddJobModel.objects.all()
    
    jobdict={
        'jobdata':jobdata
    }
    
    return render(request,'joblist.html',jobdict)

def logoutPage(request):
    logout(request)

    return redirect('signinPage')

@login_required
def editjob(request,editid):
    editdata = AddJobModel.objects.get(id=editid)
    
    datadict={
        'editdata':editdata
    }
    
    return render(request,'Recuriter/editjob.html',datadict)

@login_required
def UpdateJob(request):
    if request.method=='POST':
        jobid=request.POST.get('jobid')
        jobTitle=request.POST.get('jobTitle')
        companyName=request.POST.get('companyName')
        companyAddress=request.POST.get('companyAddress')
        description=request.POST.get('description')
        salary=request.POST.get('salary')
        experiences=request.POST.get('experiences')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        
        current_user = request.user
        
        updatejobdata = AddJobModel(
            id = jobid,
            JobTitle=jobTitle,
            CompanyName=companyName,
            CompanyAddress=companyAddress,
            Designation=designation,
            JobDescription=description,
            Salary=salary,
            Experience=experiences,
            Deadline=deadline,
            Created_by=current_user,
        )
        updatejobdata.save()
        return redirect('JobList')

@login_required   
def deletejob(request,deleteid):
    deletedata = AddJobModel.objects.get(id=deleteid)
    deletedata.delete()
    
    return redirect('JobList')

@login_required
def viewjob(request,viewid):
    viewjobdata = AddJobModel.objects.get(id=viewid)
    viewdict={
        'viewjobdata':viewjobdata
    }
    
    return render(request,'viewjob.html',viewdict)

@login_required
def editprofilePage(request):
    current_user=request.user
    current_usertype=request.user.UserType
    if request.method=='POST':
        email=request.POST.get('email')
        fullName=request.POST.get('fullName')
        address=request.POST.get('address')
        dateOfBirth=request.POST.get('dateOfBirth')
        nationality=request.POST.get('nationality')
        religion=request.POST.get('religion')
        mobile=request.POST.get('mobile')

        companyName=request.POST.get('companyName')
        companyAddress=request.POST.get('companyAddress')
        preimg=request.POST.get('preimg')
        profileimg=request.FILES.get('profileimg')
        pass_word=request.POST.get('password')
        cnfpassword=request.POST.get('cnfpassword')
        

        
        if pass_word == cnfpassword:
            if check_password(pass_word, current_user.password):
                current_user.email = email
                current_user.FullName = fullName
                current_user.Address = address
                current_user.basicinfomodel.DateOfBirth = dateOfBirth
                current_user.contactinfomodel.Mobile = mobile
                current_user.save()
                current_user.contactinfomodel.save()
                return redirect("basicinfo")
            
        
    
    return render(request,'editprofile.html')


@login_required
def basicinfo(request):
    
    return render(request,'basicinfo.html')

@login_required
def contactinfo(request):
    
    return render(request,'contact.html')
@login_required
def changePasswordPage(request):
    
    return render(request,'changepasswordpage.html')