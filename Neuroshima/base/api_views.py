from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tournaments, News
from .serializers import NewsSerializer


@api_view()
def first_api_view(request):
    num_tournaments = Tournaments.objects.count()
    return Response({"num_tournaments": num_tournaments})

@api_view()
def all_news(request):
    news = News.objects.all()
    news_serializer = NewsSerializer(news, many = True)
    return Response(news_serializer.data)