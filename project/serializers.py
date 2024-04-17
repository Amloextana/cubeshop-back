from .models import *
from rest_framework import serializers
from collections import OrderedDict
 
class UserSerializer(serializers.ModelSerializer):
    is_moderator = serializers.BooleanField(default=False, required=False)
    class Meta:
        model = Users
        fields = ['email', 'password', 'is_moderator'] 

class UserAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['email'] 

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Components
        fields = "__all__"
 
class ApplicationSerializer(serializers.ModelSerializer):
    customer = UserAppSerializer(read_only=True)
    class Meta:
        model = Applications
        fields = "__all__"
        
 
class ApplicationscomponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicationscomponents
        fields = '__all__'
