#
from .auth import User

#rest_framework
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "username"
    permission_classes = [IsOwnerOrReadOnly]
    
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def toggle_follow(self, request, pk=None):
        user = request.user
        user_profile = self.get_object()#target user account
        if user.follows.filter(id=user_profile.id).exists():
            user.follows.remove(user_profile)
            following = False
        else:
            user.follows.add(user_profile)
            following = True
        user.save()
        user_profile_follows = user_profile.follows.count() #how many accounts follow target user after update
        
        serializer = self.get_serializer(user_profile, context={"request":request})
        return Response({ "following":following, "follows":user_profile_follows }, status=status.HTTP_200_OK)
        
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user").prefetch_related("like").all().order_by("-date")
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get("username")
        if username:
            queryset = queryset.filter(user__username=username)
        return queryset
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def toggle_like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        if post.like.filter(id=user.id).exists():
            post.like.remove(user)
            liked = False
        elif not post.like.filter(id=user.id).exists():
            post.like.add(user)
            liked = True
        post.save()
        
        serializer = self.get_serializer(post, context={"request": request})
        
        return Response({
            "liked":liked,
            "likes":post.like.count(),
            "post":serializer.data
        }, status=status.HTTP_200_OK)