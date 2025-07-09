from django.contrib import admin
from django.urls import path, include
from django.conf import settings # access to the setting.py file
from django.conf.urls.static import static # method to create URLS for static files


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)