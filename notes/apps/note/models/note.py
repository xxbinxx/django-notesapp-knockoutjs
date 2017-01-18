import os

from autoslug.fields import AutoSlugField
from autoslug.utils import slugify
from django.contrib.auth.models import User
from django.db import models

from notes import settings

#-------------------------------------------------------------------------------
# get_upload_path
#-------------------------------------------------------------------------------
def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    img_name = "{}.{}".format(slugify(instance.title), ext)
    
    fullname = os.path.join(settings.MEDIA_ROOT, 'notes', img_name)
    
    #Remove any previous files with same name.
    if os.path.exists(fullname):
        os.remove(fullname)
        
    return img_name

#-------------------------------------------------------------------------------
# Note
#-------------------------------------------------------------------------------
class ModelNote(models.Model):
    
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title", unique=True)
    content = models.TextField()
    Author = models.ForeignKey(User)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
#     tags = models.ManyToManyField(ModelNoteTag, related_name='notes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        db_table = "note"
    
    #---------------------------------------------------------------------------
    # __str__
    #---------------------------------------------------------------------------
    def __str__(self):
        return self.title
