from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from notes.apps.note.api.views.note import ViewAPINote


router = routers.DefaultRouter()
router.register(r'notes', ViewAPINote, 'notes')

urlpatterns = [
    url(r'^', include(router.urls)),
] 
