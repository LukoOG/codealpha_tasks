from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.storage import staticfiles_storage

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

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "image", "available"]


# Category serializer (with nested menu items)
class CategorySerializer(serializers.ModelSerializer):
    items = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "items"]
        
class RestaurantSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    banner = serializers.SerializerMethodField()
    
    class Meta:
        model = Restaurant
        fields = [
            "id", "name", "image", "banner", "description", "location",
            "avg_rating", "review_count", "delivery_time", "delivery_fee",
            "is_open", "is_favorite"
        ]
    
    def get_is_favorite(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return obj.favorites.filter(id=user.id).exists()
        return False
    def get_image(self, obj):
        return staticfiles_storage.url(obj.image.url) if obj.image else None
    def get_banner(self, obj):
        return staticfiles_storage.url(obj.banner.url) if obj.banner else None
      
class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["id", "name", "image", "description", "avg_rating", "delivery_time", "delivery_fee"]


class RestaurantProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ["categories"]
       