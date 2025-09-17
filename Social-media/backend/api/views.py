#
from .models import Restaurant, Cart, Product, CartItem
from .auth import User

#rest_framework
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import RestaurantSerializer, RestaurantListSerializer, RestaurantProductSerializer, CartSerializer, CartItemSerializer

#rest_framework simple jwts


#View Functions
@api_view(["GET"])
def index(request):
    context = {
        'list of url routes': '/index',
    }
    return Response(context)