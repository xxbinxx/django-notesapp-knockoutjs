

from django.conf.urls import url

from notes.apps.note.views.home import ViewNotesHome


urlpatterns = [
    url(r'^', ViewNotesHome.as_view(), name='home'),    
]
