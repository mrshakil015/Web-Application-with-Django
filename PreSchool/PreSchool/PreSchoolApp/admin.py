from django.contrib import admin
from PreSchoolApp.models import *
# Register your models here.

class customeUserDisplay(admin.ModelAdmin):
    list_display = ['username','email','UserType']
    
    search_fields=["username","UserType",'email']
    
    fieldsets = [
        (
            "Users",
            {"fields":["username","email","UserType","ProfilePic"]}
        )
    ]
    
admin.site.register(customeUser,customeUserDisplay)