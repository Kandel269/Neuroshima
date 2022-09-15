from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Tournaments, News, Armies
from .serializers import NewsSerializer, ArmiesSerializer


@api_view()
def first_api_view(request):
    num_tournaments = Tournaments.objects.count()
    return Response({"num_tournaments": num_tournaments})

# @api_view()
# def all_news(request):
#     news = News.objects.all()
#     news_serializer = NewsSerializer(news, many = True)
#     return Response(news_serializer.data)

class AllNews(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class AllArmies(ListAPIView):
    queryset = Armies.objects.all()
    serializer_class = ArmiesSerializer