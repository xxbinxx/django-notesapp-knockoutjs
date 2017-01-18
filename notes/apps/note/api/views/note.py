import logging

from rest_framework.viewsets import ModelViewSet

from notes.apps.note.api.serializers.note import SerializerNote
from notes.apps.note.models.note import ModelNote


logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
# ViewAPINote
#-------------------------------------------------------------------------------
class ViewAPINote(ModelViewSet):
     
    serializer_class = SerializerNote
    queryset = ModelNote.objects.all()
    