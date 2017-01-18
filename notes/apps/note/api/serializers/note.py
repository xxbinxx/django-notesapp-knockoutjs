from rest_framework import serializers

from notes.apps.account.api.serializers.user import SerializerUser
from notes.apps.note.models.note import ModelNote


#-------------------------------------------------------------------------------
# SerializerNote
#-------------------------------------------------------------------------------
class SerializerNote(serializers.ModelSerializer):
    
    Author = SerializerUser()
    
    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        
        model = ModelNote
        fields = ('id', 'title', 'content', 'Author', 'image', 'created', 'updated')
        