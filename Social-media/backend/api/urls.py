from . import views, auth
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserProfileViewSet, basename="user")
router.register(r'posts', views.PostViewSet, basename="post")

urlpatterns = [
    #path('', views.index, name=""),
    #auth routes
    path('auth/register', auth.RegisterView.as_view(), name='register'),
    path('auth/login', auth.LoginTokenObtainPairView.as_view(), name='login'),
    path("auth/logout", auth.LogoutView.as_view(), name="logout"),
    path('auth/token/refresh', auth.CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls))
    
]