from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('seeker','JobSeekter')
    ]
    
    BLOODGROUP = [
        ('a+','A+'),('b+','B+'),('o+','O+'),('ab+','AB+'),('ab-','AB-')
    ]
    
    displayname=models.CharField(max_length=100,null=True)
    fathername=models.CharField(max_length=100,null=True)
    mothername=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    profileimg=models.ImageField(upload_to='media/img/',null=True)
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    blood_group=models.CharField(choices=BLOODGROUP,max_length=100,null=True)
    
class AddJobModel(models.Model):
    RecruiterName=models.CharField(max_length=100,null=True)
    JobTitle=models.CharField(max_length=100,null=True)
    CompanyName=models.CharField(max_length=100,null=True)
    CompanyDescription=models.TextField(null=True)
    JobDescription=models.TextField(null=True)
    Qualification=models.CharField(max_length=100,null=True)
    Salary=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    Experience=models.CharField(max_length=100,null=True)
    Deadline=models.CharField(max_length=100,null=True)
    Created_by = models.ForeignKey(Custom_User,on_delete=models.CASCADE, null=True)
    
    
class jobSeekerProfile(models.Model):
    myUser = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='jobseekerprofile')
    skills=models.CharField(max_length=100,null=True)
    work_experience=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.myUser.username+ " - "+self.myUser.user_type

class jobRecruiterProfile(models.Model):
    myUser = models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='jobrecruiterprofile')
    company_name=models.CharField(max_length=100,null=True)
    company_address=models.CharField(max_length=100,null=True)
    
    def __str__(self) -> str:
        return self.myUser.username+ " - "+self.myUser.user_type
