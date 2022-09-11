from django.urls import path
from . import views
from .views import RoomListView, RoomView, MessageDeleteView, RoomCreateView

app_name = 'chat'
urlpatterns = [
    path('lista-pokojów/',RoomListView.as_view(), name='room_list_view'),
    path('pokój/<str:id>/',RoomView.as_view(), name='room_view'),
    path('usuń-wiadomość/<str:pk>/<str:id>/',MessageDeleteView.as_view(), name='delete_message'),
    path('stwórz-pokój',RoomCreateView.as_view(), name='room_create'),
]