from django.contrib import admin
from django.urls import path
from portfolioProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name="homePage"),
    # path('studentPage/',studentPage,name="studentPage"),/
]
