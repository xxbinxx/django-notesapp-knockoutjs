from django.contrib import admin

from notes.apps.note.models.note import ModelNote
from notes.apps.note.models.tag import ModelNoteTag


#-------------------------------------------------------------------------------
# AdminModelNote
#-------------------------------------------------------------------------------
class AdminModelNote(admin.ModelAdmin):
    model = ModelNote
    
admin.site.register(ModelNote, AdminModelNote)


#-------------------------------------------------------------------------------
# AdminModelNoteTag
#-------------------------------------------------------------------------------
class AdminModelNoteTag(admin.ModelAdmin):
    model = ModelNoteTag
    
admin.site.register(ModelNoteTag, AdminModelNoteTag)
