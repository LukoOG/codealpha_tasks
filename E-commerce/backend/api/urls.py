from . import views, auth
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#restaurant_router = DefaultRouter()

#restaurant_router.register(r'', views.RestaurantViewSet, basename="restaurnts")

urlpatterns = [
    path('', views.index, name=""),
    #auth routes
    path('auth/register', auth.RegisterView.as_view(), name='register'),
    path('auth/login', auth.LoginTokenObtainPairView.as_view(), name='login'),
    path("auth/logout", auth.LogoutView.as_view(), name="logout"),
    path('auth/token/refresh', auth.CustomTokenRefreshView.as_view(), name="token_refresh"),
    
    #view routes
    #path("restaurants/", include(restaurant_router.urls)),
    path("restaurants/", views.RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurants/<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
]