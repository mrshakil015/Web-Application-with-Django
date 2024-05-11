from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobPortalProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinPage,name="signinPage"),
    path('signupPage/',signupPage,name="signupPage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('profile/',profile,name="profile"),
    path('AppliedJob/',AppliedJob,name="AppliedJob"),
    path('JobList/',JobList,name="JobList"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    path('editprofilePage/',editprofilePage,name="editprofilePage"),
    path('basicinfo/',basicinfo,name="basicinfo"),
    path('contactinfo/',contactinfo,name="contactinfo"),
    path('changePasswordPage/',changePasswordPage,name="changePasswordPage"),
    
    path('AddJob/',AddJob,name="AddJob"),
    path('editjob/<str:editid>',editjob,name="editjob"),
    path('UpdateJob/',UpdateJob,name="UpdateJob"),
    path('deletejob/<str:deleteid>',deletejob,name="deletejob"),
    path('viewjob/<str:viewid>',viewjob,name="viewjob"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
