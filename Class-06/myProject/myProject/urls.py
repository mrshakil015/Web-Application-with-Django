from django.contrib import admin
from django.urls import path
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentpage/', studentpage, name='studentpage'),
    path('teacherpage/', teacherpage, name='teacherpage'),
    path('staffpage/', staffpage, name='staffpage'),
    path('managementpage/', managementpage, name='managementpage'),
    path('librarypage/', librarypage, name='librarypage'),
]
