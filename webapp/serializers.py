from django.contrib.auth.models import User  
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from . models import employees
from webapp import models
class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']