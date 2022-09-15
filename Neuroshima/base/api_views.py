from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tournaments

@api_view()
def first_api_view(request):
    num_tournaments = Tournaments.objects.count()
    return Response({"num_tournaments": num_tournaments})