from django.contrib import admin
from .models import *

# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display = ['username','Name','Age']
admin.site.register(CustomeUserModel,UserDisplay)

class CaloriesDisplay(admin.ModelAdmin):
    list_display = ['ItemName','CaloriesConsumed']
admin.site.register(CaloriesModel,CaloriesDisplay)
