from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseekter','JobSeekter')
    ]
    
    displayname=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=100)
    

