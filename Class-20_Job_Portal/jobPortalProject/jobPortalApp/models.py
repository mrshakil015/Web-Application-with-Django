from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseekter','JobSeekter')
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
    

