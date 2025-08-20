from . import views, auth
from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.index, name=""),
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('login', auth.EmailTokenObtainPairView.as_view(), name='login'),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh")
]