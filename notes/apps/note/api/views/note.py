import logging

from rest_framework.viewsets import ModelViewSet

from notes.apps.note.api.serializers.note_read import SerializerNoteRead
from notes.apps.note.api.serializers.note_write import SerializerNoteWrite
from notes.apps.note.models.note import ModelNote


logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
# ViewAPINote
#-------------------------------------------------------------------------------
class ViewAPINote(ModelViewSet):
     
    queryset = ModelNote.objects.all()
    create_serializer_class = SerializerNoteWrite
    read_serializer_class = SerializerNoteRead
    
    #---------------------------------------------------------------------------
    # get_serializer_class
    #---------------------------------------------------------------------------
    def get_serializer_class(self):
        
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return self.create_serializer_class

        return self.read_serializer_class