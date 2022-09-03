from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Room


class RoomListView(TemplateView):
    template_name = 'forum/room_list.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['room_list'] = Room.objects.all()
        return context

