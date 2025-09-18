#
from .auth import User

#rest_framework
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .serializers import UserProfileSerializer, PostSerializer
from .models import *
#rest_framework simple jwts


#View Functions
@api_view(["GET"])
def index(request):
    context = {
        'list of url routes': '/index',
    }
    return Response(context)
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user").prefetch_related("like").all().order_by("-date")
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(user__username=username)
        return queryset