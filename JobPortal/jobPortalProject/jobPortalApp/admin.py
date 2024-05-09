from django.contrib import admin
from jobPortalApp.models import *

# Register your models here.

class Job_User_Display(admin.ModelAdmin):
    list_display = ['FullName','username','UserType']
    
class Add_Job_List_Display(admin.ModelAdmin):
    list_display = ['JobTitle','Created_by','CompanyName']
    
admin.site.register(Job_User,Job_User_Display)
admin.site.register(AddJobModel,Add_Job_List_Display)
admin.site.register(RecruiterProfileModel)
admin.site.register(SeekerProfileModel)
admin.site.register(BasicInfoModel)
admin.site.register(EducationalModel)
admin.site.register(WorkExperinceModel)
admin.site.register(contactModel)
