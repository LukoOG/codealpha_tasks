from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .manager import User

from rest_framework import serializers
from api.models import *

user = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = user
        fields = [
            'id', 'email', 'password'
        ]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterUserSerializer, self).create(validated_data)
        # password = validated_data.pop('password')
        # user = User.objects.create(**validated_date)
        # return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = [
            'id', 'email', 'first_name', 'last_name', 'phone_number', 'shipping_address'
        ]