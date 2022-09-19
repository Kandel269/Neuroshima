from django.urls import path
from . import views
from .views import RoomListView, RoomView, MessagesDeleteView, RoomCreateView, RoomDeleteView, RoomUpdateView, \
    MessagesUpdateView
from django.contrib.auth.decorators import login_required


app_name = 'chat'
urlpatterns = [
    path('lista-pokojow/',RoomListView.as_view(), name='room_list_view'),
    path('pokoj/<str:id>/',RoomView.as_view(), name='room_view'),
    path('usun-wiadomosc/<str:pk>/', login_required(MessagesDeleteView.as_view()), name='delete_message'),
    path('edytuj-wiadomosc/<str:pk>/', login_required(MessagesUpdateView.as_view()), name='update_message'),

    path('stworz-pokoj',RoomCreateView.as_view(), name='room_create'),
    path('usun-pokoj/<str:pk>/',login_required(RoomDeleteView.as_view()), name='room_delete'),
    path('edytuj-pokoj/<str:pk>/',login_required(RoomUpdateView.as_view()), name='room_update'),

]