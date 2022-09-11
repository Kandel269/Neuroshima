from django.urls import path
from . import views
from .views import RoomListView, RoomView, MessagesDeleteView, RoomCreateView, RoomDeleteView, RoomUpdateView, \
    MessagesUpdateView
from django.contrib.auth.decorators import login_required


app_name = 'chat'
urlpatterns = [
    path('lista-pokojów/',RoomListView.as_view(), name='room_list_view'),
    path('pokój/<str:id>/',RoomView.as_view(), name='room_view'),
    path('usuń-wiadomość/<str:pk>/<str:id>/', login_required(MessagesDeleteView.as_view()), name='delete_message'),
    path('edytuj-wiadomość/<str:pk>/<str:id>/', login_required(MessagesUpdateView.as_view()), name='update_message'),

    path('stwórz-pokój',RoomCreateView.as_view(), name='room_create'),
    path('usuń-pokój/<str:pk>/',login_required(RoomDeleteView.as_view()), name='room_delete'),
    path('edytuj-pokój/<str:pk>/',login_required(RoomUpdateView.as_view()), name='room_update'),

]