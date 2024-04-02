from django.contrib import admin
from django.urls import path
from portfolioProject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name="homePage"),
    path('aboutPage/',aboutPage,name="aboutPage"),
    path('educationPage/',educationPage,name="educationPage"),
    path('resumePage/',resumePage,name="resumePage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
