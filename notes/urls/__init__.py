"""
            Notes URL Configuration
"""

import os

from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from notes import settings

admin.autodiscover()

urlpatterns = [
               
    url(r'^admin/', admin.site.urls),
    
    url(r'^', include('notes.apps.note.urls', namespace='note')),
    
    url(r'^api/', include('notes.urls.api', namespace='api'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
