from django.urls import path
from . import views
from .views import RoomListView, RoomView, MessagesDeleteView, RoomCreateView, RoomDeleteView, RoomUpdateView, \
    MessagesUpdateView

app_name = 'chat'
urlpatterns = [
    path('lista-pokojów/',RoomListView.as_view(), name='room_list_view'),
    path('pokój/<str:id>/',RoomView.as_view(), name='room_view'),
    path('usuń-wiadomość/<str:pk>/<str:id>/', MessagesDeleteView.as_view(), name='delete_message'),
    path('edytuj-wiadomość/<str:pk>/<str:id>/', MessagesUpdateView.as_view(), name='update_message'),

    path('stwórz-pokój',RoomCreateView.as_view(), name='room_create'),
    path('usuń-pokój/<str:pk>/',RoomDeleteView.as_view(), name='room_delete'),
    path('edytuj-pokój/<str:pk>/',RoomUpdateView.as_view(), name='room_update'),

]