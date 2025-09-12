from . import views, auth
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cart', views.CartViewSet, basename="cart")
router.register(r'cart-items', views.CartItemViewSet, basename="cart-items")

urlpatterns = [
    path('', views.index, name=""),
    #auth routes
    path('auth/register', auth.RegisterView.as_view(), name='register'),
    path('auth/login', auth.LoginTokenObtainPairView.as_view(), name='login'),
    path("auth/logout", auth.LogoutView.as_view(), name="logout"),
    path('auth/token/refresh', auth.CustomTokenRefreshView.as_view(), name="token_refresh"),
    
    #view routes
    path("restaurants/", views.RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurants/<int:pk>/", views.RestaurantDetailView.as_view(), name="restaurant-detail"),
    
    path("", include(router.urls)),
]