#
from .models import Restaurant

#rest_framework
from rest_framework import viewsets, permissions, status, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import RestaurantSerializer, RestaurantListSerializer, RestaurantProductSerializer

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