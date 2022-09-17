from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authtoken.models import Token

from .models import Tournaments, News, Armies
from .serializers import NewsSerializer, ArmiesSerializer


class Login(APIView):

    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Dane są błędne lub użytkownik nie istnieje'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token':token.key}, status=HTTP_200_OK)

@api_view()
def first_api_view(request):
    num_tournaments = Tournaments.objects.count()
    return Response({"num_tournaments": num_tournaments})

class AllNews(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = []
    permission_classes = []

class AllArmies(ListAPIView):
    queryset = Armies.objects.all()
    serializer_class = ArmiesSerializer
    authentication_classes = []
    permission_classes = []


