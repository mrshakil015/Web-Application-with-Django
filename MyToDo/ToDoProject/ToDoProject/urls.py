from django.contrib import admin
from django.urls import path
from ToDoProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard,name="dashboard")
]
