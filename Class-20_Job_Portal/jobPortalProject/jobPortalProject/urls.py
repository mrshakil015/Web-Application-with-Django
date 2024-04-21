from django.contrib import admin
from django.urls import path
from jobPortalProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name="signup"),
    path('',signin,name="signin"),
]
