#rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#rest_framework simple jwts
#View Functions
@api_view(["GET"])
def index(request):
    context = {
        'list of url routes': '/index',
    }
    return Response(context)

