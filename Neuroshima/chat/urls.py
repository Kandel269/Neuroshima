from django.urls import path
from . import views
from .views import RoomListView, RoomView

urlpatterns = [
    path('forum/lista-pokojów/',RoomListView.as_view(), name='room_list_view'),
    path('forum/pokój/<str:id>/',RoomView.as_view(), name='room_detail_view'),
]