from djoser.serializers import UserCreateSerializer,UserSerializer
from rest_framework import serializers
from .models import *
# from api.settings import AUTH_USER_MODEL

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=['id','email','username','password','user_type','is_staff']


class Collegeserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = College
        fields = ['id','phone','college_id','city','user','user_id']


class Studentserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Students
        fields = ['college','student_name','profile_pic','enrollment','semester','department','user','user_id']


class Professorserializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Professors
        fields = '__all__'