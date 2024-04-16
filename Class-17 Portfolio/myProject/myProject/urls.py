from django.contrib import admin
from django.urls import path
from myProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('resume/',resume,name="resume"),
    path('contact/',contact,name="contact"),
    path('edithome/',edithome,name="edithome"),
    path('editabout/',editabout,name="editabout"),
    path('editeducation/',editeducation,name="editeducation"),
    path('editwork/',editwork,name="editwork"),
    path('editcontact/',editcontact,name="editcontact"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
