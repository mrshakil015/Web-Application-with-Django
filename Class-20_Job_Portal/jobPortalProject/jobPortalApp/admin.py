from django.contrib import admin
from jobPortalApp.models import *

class Custom_User_Display(admin.ModelAdmin):
    list_display=['displayname','user_name']
    
admin.site.register(Custom_User,Custom_User_Display)
