from django.contrib.auth import get_user_model
from django.conf import settings

from .serializers import RegisterUserSerializer

#rest_framework
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            data = response.data
            access = data.get("access")
            refresh = data.get("refresh")
            print(access)

            # Set cookies
            response.set_cookie(
                key="accessToken",
                value=access,
                httponly=True,
                secure=True,  
                samesite="None",
                max_age=60 * 15,
            )
            
            response.set_cookie(
                key="refreshToken",
                value=refresh,
                httponly=True,
                secure=True,
                samesite="None",
                max_age=60 * 60 * 24 * 7,
            )

            del response['access']
            del response['refresh']
        return response
    
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh = request.COOKIES.get("refreshToken")
        if refresh is None:
            return Response({"detail": "Refresh token missing"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            token = RefreshToken(refresh)
            access = str(token.access_token)
        except Exception:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
        
        response = Response({"success": True})
        response.set_cookie(
            key="accessToken",
            value=access,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=60 * 15,
        )
        return response
    
class LogoutView(APIView):
    def post(self, request):
        response = Response({"success": True})
        response.delete_cookie("accessToken")
        response.delete_cookie("refreshToken")
        return response