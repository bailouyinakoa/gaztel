from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns = [
    path('elinels/', admin.site.urls),
    path('',include("DjuigiFaune.urls")),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()