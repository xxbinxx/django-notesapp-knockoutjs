from rest_framework import serializers

from notes.apps.account.api.serializers.user import SerializerUser
from notes.apps.note.models.note import ModelNote


#-------------------------------------------------------------------------------
# SerializerNoteRead
#-------------------------------------------------------------------------------
class SerializerNoteRead(serializers.ModelSerializer):
    
#     Author = SerializerUser()
    Author = serializers.SerializerMethodField()
    
    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        
        model = ModelNote
        fields = ('id', 'title', 'content', 'Author', 'image',)
        
        
    #---------------------------------------------------------------------------
    # get_author
    #---------------------------------------------------------------------------
    def get_Author(self, note):
        return note.Author.first_name or note.Author.username