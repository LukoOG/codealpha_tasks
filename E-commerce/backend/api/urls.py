from . import views, auth
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.index, name=""),
    #auth routes
    path('auth/register/', auth.RegisterView.as_view(), name='register'),
    path('auth/login', auth.EmailTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name="token_refresh")
]