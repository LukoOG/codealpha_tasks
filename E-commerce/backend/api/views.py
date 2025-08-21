#django
from django.contrib.auth.decorators import login_required

#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#rest_framework simple jwts
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

#View Functions
@api_view(["GET"])
def index(request):
    context = {
        'list of url routes': '/index',
    }
    return Response(context)

