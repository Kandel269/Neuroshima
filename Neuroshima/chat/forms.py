from django import forms

from .models import Messages, Room


class MessagesForm(forms.ModelForm):

    class Meta:
        model = Messages
        fields = ['body']

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name','topic','description']

