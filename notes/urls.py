"""
            Notes URL Configuration
"""

from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from notes import settings

admin.autodiscover()

urlpatterns = [
               
    url(r'^admin/', admin.site.urls),
    url(r'^api/?', include('notes.apps.note.api.urls'), name='api'),
    url(r'^', include('notes.apps.note.urls', namespace='note'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
