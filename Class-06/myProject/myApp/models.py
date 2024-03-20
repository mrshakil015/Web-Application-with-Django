from django.db import models

# Create your models here.
class studentModel(models.Model):
    roll=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name +"-"+self.roll
    
class teacherModel(models.Model):
    teacherid=models.CharField(max_length=20)
    teachername=models.CharField(max_length=50)
    teacherdesignation=models.CharField(max_length=50)
    
    def __str__(self):
        return self.teachername +"-"+self.teacherid

class staffModel(models.Model):
    staffid=models.CharField(max_length=20)
    staffname=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    
    def __str__(self):
        return self.staffname +"-"+self.staffid

class managementModel(models.Model):
    managementid=models.CharField(max_length=20)
    managementname=models.CharField(max_length=50)
    
    def __str__(self):
        return self.managementname +"-"+self.managementid

class libraryModel(models.Model):
    libraryid=models.CharField(max_length=20)
    librarylocation=models.CharField(max_length=50)
    
    def __str__(self):
        return self.libraryid +"-"+self.librarylocation

