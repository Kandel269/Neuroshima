from django.urls import path
from . import views
from .views import RoomListView

urlpatterns = [
    path('lista-pokojów',RoomListView.as_view(), name='room_list_view')
]