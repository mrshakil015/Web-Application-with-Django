from django.contrib import admin
from django.urls import path
from PreSchool.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage/',signupPage,name="signupPage"),
    path('signinPage/',signinPage,name="signinPage"),
    
    #--------Teacher Route--------------
    path('teacherDashboard/',teacherDashboard,name="teacherDashboard"),
    
    #--------Admin Route--------------
    path('adminDashboard/',adminDashboard,name="adminDashboard"),
    
    #--------Students Route--------------
    path('studentDashboard/',studentDashboard,name="studentDashboard"),
    path('addStudent/',addStudent,name="addStudent"),
    path('editStudent/',editStudent,name="editStudent"),
    path('studentList/',studentList,name="studentList"),
    
    
    
    path('componentPage/',componentPage,name="componentPage"),
]
