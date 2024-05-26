from django.contrib import admin
from django.urls import path
from PreSchool.views import *
from PreSchool.teacherviews import *
from PreSchool.studentviews import *
from PreSchool.departmentviews import *
from PreSchool.subjectviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage/',signupPage,name="signupPage"),
    path('',signinPage,name="signinPage"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    
    #--------Teacher Route--------------
    path('teacherDashboard/',teacherDashboard,name="teacherDashboard"),
    path('addTeacher/',addTeacher,name="addTeacher"),
    path('editTeacher/',editTeacher,name="editTeacher"),
    path('teacherDetails/',teacherDetails,name="teacherDetails"),
    path('teacherList/',teacherList,name="teacherList"),
    
    #--------Admin Route--------------
    path('adminDashboard/',adminDashboard,name="adminDashboard"),
    
    #--------Students Route--------------
    path('studentDashboard/',studentDashboard,name="studentDashboard"),
    path('addStudent/',addStudent,name="addStudent"),
    path('editStudent/',editStudent,name="editStudent"),
    path('studentList/',studentList,name="studentList"),
    path('studentDetails/',studentDetails,name="studentDetails"),
    
    #--------Department Route--------------
    path('addDepartment/',addDepartment,name="addDepartment"),
    path('editDepartment/',editDepartment,name="editDepartment"),
    path('departmentList/',departmentList,name="departmentList"),
    
    #--------Subject Route--------------
    path('addSubject/',addSubject,name="addSubject"),
    path('editSubject/',editSubject,name="editSubject"),
    path('subjectList/',subjectList,name="subjectList"),
    
    
]
