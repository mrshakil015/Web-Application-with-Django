from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Job_User(AbstractUser):
    USER = [
        ('Recuriter','Recuriter'),
        ('Seeker','Seeker')
    ]
    
    FullName = models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    UserType= models.CharField(choices=USER,max_length=100)
    ProfileImage = models.ImageField(upload_to='static/img/')
    
class AddJobModel(models.Model):
    JobTitle= models.CharField(max_length=100,null=True)
    CompanyName= models.CharField(max_length=100,null=True)
    CompanyAddress= models.CharField(max_length=100,null=True)
    Designation= models.CharField(max_length=100,null=True)
    JobDescription= models.TextField(null=True)
    Salary= models.CharField(max_length=100,null=True)
    Experience= models.CharField(max_length=100,null=True)
    Deadline= models.CharField(max_length=100,null=True)
    Created_by=models.ForeignKey(Job_User,on_delete=models.CASCADE,null=True)
    
class RecruiterProfileModel(models.Model):
    myUser = models.OneToOneField(Job_User,on_delete=models.CASCADE, related_name='recuriterprofile',null=True)
    CompanyName = models.CharField(max_length=100)
    CompanyAddress = models.CharField(max_length=100)
    
    LAST_WORK = [
        ('dipti','DIPTI'),
        ('dit','DIT'),
    ]
    
    LastWork = models.CharField(choices=LAST_WORK, max_length=50)
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType+" - "+self.CompanyName
    
class SeekerProfileModel(models.Model):
    myUser = models.OneToOneField(Job_User,on_delete=models.CASCADE, related_name='seekerprofile',null=True)
    Skills = models.CharField(max_length=100)
    Work_Experience = models.CharField(max_length=100)
    LAST_EDUCATION=[
        ('jsc','JSC'),
        ('ssc','SSC'),
        ('hsc','HSC'),
        ('bsc','BSC'),
    ]
    
    LastEducation = models.CharField(choices=LAST_EDUCATION, max_length=50)
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType

class BasicInfoModel(models.Model):
    myUser = models.OneToOneField(Job_User, on_delete=models.CASCADE, related_name='basicinfomodel')
    DateOfBirth = models.CharField(max_length=50)
    Nationality= models.CharField(max_length=50)
    Religion= models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType

class EducationalModel(models.Model):
    myUser = models.OneToOneField(Job_User, on_delete=models.CASCADE, related_name='educationalinfomodel')
    Institute= models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    PassingYear = models.CharField(max_length=50)
    CGPA = models.CharField(max_length=50)
    Grade = models.CharField(max_length=50)
    Grade2 = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType

class WorkExperinceModel(models.Model):
    myUser = models.OneToOneField(Job_User, on_delete=models.CASCADE, related_name='workinfomodel')
    CompanyName= models.CharField(max_length=50)
    Designation= models.CharField(max_length=50)
    Duration= models.CharField(max_length=50)
    Location= models.CharField(max_length=50,null=True)
    
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType

class contactModel(models.Model):
    myUser = models.OneToOneField(Job_User, on_delete=models.CASCADE, related_name='contactinfomodel')
    Mobile = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.myUser.username+" - "+self.myUser.UserType