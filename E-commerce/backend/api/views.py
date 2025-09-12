#
from .models import Restaurant, Cart
from .auth import User

#rest_framework
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import RestaurantSerializer, RestaurantListSerializer, RestaurantProductSerializer, CartSerializer

#rest_framework simple jwts


#View Functions
@api_view(["GET"])
def index(request):
    context = {
        'list of url routes': '/index',
    }
    return Response(context)

#Viewsets
class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.prefetch_related("categories__items")
    serializer_class = RestaurantProductSerializer
    
class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for listing and retrieving restaurants
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def toggle_favorite(self, request, pk=None):
        user = request.user
        restaurant = self.get_object()
        
        if restaurant.favorites.filter(id=user.id).exists():
            restaurant.favorites.remove(user.id)
            return Response({"is_false":False}, status=status.HTTP_200_OK)
        else:
            restaurant.favorites.add(user.id)
            return Response({"is_false":False}, status=status.HTTP_200_OK)           
            
            
class CartViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request):
        """the current user's Cart, not a list of all Carts"""
        user = User.objects.get(email=self.request.user)
        try:
            cart = Cart.objects.filter(user=user)
            serializer = CartSerializer(cart, many=True)
        except Cart.DoesNotExist:
            return Response({"detail": "No active Cart found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)
        
    def destroy(self, request, pk=None):
        """Delete the user's active Cart"""
        try:
            cart = Cart.objects.get(user=request.user)
            cart.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cart.DoesNotExist:
            return Response({"detail": "No active Cart found"}, status=status.HTTP_404_NOT_FOUND)
            
            
class CartItemViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        product_id = request.data.get("product")
        quantity = int(request.data.get("quantity", 1))
        
        if not product_id:
            return Response({"detail": "Product ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Invalid product"}, status=status.HTTP_404_NOT_FOUND)
            
            
        cart, _ = Cart.objects.get_or_create(user=request.user, status="pending")
        
        if not cart.restaurant:
            cart.restaurant = product.restaurant
            cart.save()
            
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            item.quantity = quantity
        else:
            item.quantity += quantity
        item.save()
        
        serializer = CartItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk=None):
        try:
            item = CartItem.objects.get(pk=pk, cart__user=request.user)
        except Item.DoesNotExist:
            return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        quantity = int(request.data.get("quantity", 1))
        if quantity <= 0:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        item.quantity = quantity
        item.save()
        serializer = CartItemSerializer(item)
        return Response(serializer.data)
        
    def delete(self, request, pk=None):
        try:
            item = CartItem.objects.get(pk=pk)
        except item.DoesNotExist:
            return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)