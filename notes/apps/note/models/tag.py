from autoslug.fields import AutoSlugField
from django.db import models


#-------------------------------------------------------------------------------
# ModelNoteTag
#-------------------------------------------------------------------------------
class ModelNoteTag(models.Model):
    
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "note_tag"
    
    #---------------------------------------------------------------------------
    # __str__
    #---------------------------------------------------------------------------
    def __str__(self):
        return self.title
    