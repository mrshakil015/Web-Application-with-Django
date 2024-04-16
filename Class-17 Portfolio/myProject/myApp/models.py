from django.db import models

# Create your models here.
class HomeModel(models.Model):
    Name=models.CharField(max_length=30,null=True)
    ShortTitle=models.CharField(max_length=50,null=True)
    Background=models.ImageField(upload_to='static/assets/img/my/')
    
class AboutModel(models.Model):
    Name=models.CharField(max_length=30,null=True)
    Title=models.TextField(null=True)
    AboutMe=models.TextField(null=True)
    Degree=models.CharField(max_length=30,null=True)
    Phone=models.CharField(max_length=30,null=True)
    Email=models.CharField(max_length=30,null=True)
    Address=models.CharField(max_length=30,null=True)
    Photo=models.ImageField(upload_to='static/assets/img/my/',null=True)
    
class EducationModel(models.Model):
    Degree=models.CharField(max_length=50)
    Institute=models.CharField(max_length=50)
    Session=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)

class WorkModel(models.Model):
    Institute=models.CharField(max_length=100)
    Designation=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)
    Summary=models.TextField()

    
    
    