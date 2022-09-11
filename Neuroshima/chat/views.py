
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView

from .models import Room, Messages


class RoomListView(TemplateView):
    template_name = 'forum/room_list.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['room_list'] = Room.objects.all()
        return context

class RoomView(View):
    template_name = 'forum/room.html'

    def get(self,request,id=None,*args,**kwargs):
        context = {}
        if id is not None:
            room = get_object_or_404(Room, id=id)
            context['room'] = room
            context['messages'] = Messages.objects.filter(room=id)
        return render(request,self.template_name,context)