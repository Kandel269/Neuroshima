from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MessagesForm, RoomForm
from .models import Room, Messages


class RoomListView(TemplateView):
    template_name = 'forum/room_list.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['room_list'] = Room.objects.all()
        return context

class RoomView(View):
    form_class = MessagesForm
    template_name = 'forum/room.html'

    def get(self,request,id=None,*args,**kwargs):
        context = {}
        if id is not None:
            room = get_object_or_404(Room, id=id)
            context['room'] = room
            context['messages'] = Messages.objects.filter(room=id)
        return render(request,self.template_name,context)

    def post(self,request,id=None,*args,**kwargs):
        form = self.form_class(request.POST)
        if id is not None:
            room = get_object_or_404(Room, id=id)
            if form.is_valid():
                message = form.save(commit = False)
                message.room = room
                message.user = request.user
                message.save()
            return redirect('chat:room_view', id=room.id)

        return render(request,self.template_name, {})

class MessagesDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'forum/delete_message.html'
    model = Messages

    def get_success_url(self):
        return reverse('chat:room_list_view')

class MessagesUpdateView(LoginRequiredMixin,UpdateView):
    model = Messages
    fields = ['body']
    template_name = 'forum/message_update.html'

    def get_success_url(self):
        return reverse('chat:room_list_view')

class RoomCreateView(LoginRequiredMixin,CreateView):
    form_class = RoomForm
    template_name = 'forum/room_create.html'

    def get_success_url(self):
        return reverse('chat:room_list_view')

    def get(self, request, *args, **kwargs):
        context = {'form': RoomForm()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit = False)
            room.host = request.user
            room.save()
            return HttpResponseRedirect(reverse_lazy('chat:room_view', args=[room.id]))
        return render(request, self.template_name, {'form': form})

class RoomDeleteView(LoginRequiredMixin,DeleteView):
    model = Room
    template_name ='forum/room_delete.html'

    def get_success_url(self):
        return reverse('chat:room_list_view')

class RoomUpdateView(LoginRequiredMixin,UpdateView):
    model = Room
    fields = ['name','topic','description']
    template_name =  'forum/room_update.html'

    def get_success_url(self):
        return reverse('chat:room_list_view')