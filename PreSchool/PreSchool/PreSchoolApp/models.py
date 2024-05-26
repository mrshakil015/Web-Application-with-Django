from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customeUser(AbstractUser):
    USERTYPE = [
        ('1','admin'),
        ('2','teacher'),
        ('3','student'),
    ]
    
    UserType = models.CharField(choices=USERTYPE,max_length=100)
    ProfilePic = models.ImageField(upload_to='static/')
    
class StudentModel(models.Model):
    FullName = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    StudentID = models.CharField(max_length=100)
    
    GENDER  = [
        ('male','Male'),
        ('female','Female'),
    ]
    Gender = models.CharField(choices=GENDER,max_length=100)
    DateOB = models.DateField(max_length=100)
    Department = models.CharField(max_length=100)
    Religion = models.CharField(max_length=100)
    JoiningDate = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Section = models.CharField(max_length=100)
    
    FatherName = models.CharField(max_length=100)
    FatherOccupation = models.CharField(max_length=100)
    FatherMobile = models.CharField(max_length=100)
    FatherEmail = models.EmailField(max_length=100)
    
    MotherName = models.CharField(max_length=100)
    MotherOccupation = models.CharField(max_length=100)
    MotherMobile = models.CharField(max_length=100)
    MotherEmail = models.EmailField(max_length=100)
    
    PresentAddress = models.CharField(max_length=100)
    PermanentAddress = models.CharField(max_length=100)
    Added_by = models.ForeignKey(customeUser, on_delete =models.CASCADE)
    
    
    