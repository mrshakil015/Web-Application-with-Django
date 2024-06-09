from django.contrib import admin
from django.urls import path
from CalorieCounterProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinPage,name='signinPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('dashboardPage/',dashboardPage,name='dashboardPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    
    path('addPersonalInfo/',addPersonalInfo,name='addPersonalInfo'),
    path('calroyCounter/',calroyCounter,name='calroyCounter'),
]
