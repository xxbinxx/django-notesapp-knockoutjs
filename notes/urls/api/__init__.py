"""
                STORES ROOT URL PATHS FOR NOTES API's
"""

from urllib.parse import urlencode

from django.conf.urls import include
from django.conf.urls import url


urlpatterns = [
    url(r'^users/', include('notes.apps.account.api.urls', namespace='users')),
    url(r'^notes/?', include('notes.apps.note.api.urls'), name='notes'),
]
