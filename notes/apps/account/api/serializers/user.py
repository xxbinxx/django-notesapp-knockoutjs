from django.contrib.auth.models import User
from rest_framework import serializers

#-------------------------------------------------------------------------------
# SerializerUser
#-------------------------------------------------------------------------------
class SerializerUser(serializers.ModelSerializer):
    
    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        depth = 1
        