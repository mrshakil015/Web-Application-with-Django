from django.contrib import admin
from django.urls import path
from jobPortalProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('dashboard/',dashboard,name="dashboard"),
    path('addjob/',addjob,name="addjob"),
    path('viewjob/',viewjob,name="viewjob"),
    path('editjob/<str:myid>',editjob,name="editjob"),
    path('deletejob/<str:myid>',deletejob,name="deletejob"),
    path('profile/',profile,name="profile"),
    path('updatejob/',updatejob,name="updatejob"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    path('appliedJob/',appliedJob,name="appliedJob"),
    path('joblistPage/',joblistPage,name="joblistPage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
