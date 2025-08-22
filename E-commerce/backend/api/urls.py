from . import views, auth
from django.urls import path

urlpatterns = [
    path('', views.index, name=""),
    #auth routes
    path('auth/register/', auth.RegisterView.as_view(), name='register'),
    path('auth/login', auth.LoginTokenObtainPairView.as_view(), name='login'),
    path("auth/logout/", auth.LogoutView.as_view(), name="logout"),
    path('auth/token/refresh', auth.CustomTokenRefreshView.as_view(), name="token_refresh")
]