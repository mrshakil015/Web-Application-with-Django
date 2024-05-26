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