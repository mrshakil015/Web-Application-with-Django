from django.contrib import admin
from jobPortalApp.models import *

class Custom_User_Display(admin.ModelAdmin):
    list_display=['displayname','username','email','user_type']
    
class Job_Model_Display(admin.ModelAdmin):
    list_display=['JobTitle','CompanyName','Designation']
    
admin.site.register(Custom_User,Custom_User_Display)
admin.site.register(AddJobModel,Job_Model_Display)
admin.site.register(jobRecruiterProfile)
admin.site.register(jobSeekerProfile)


