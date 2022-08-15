from .models import Tournaments, DuelUser
from django.forms import ModelForm
from django import forms

class TournamentForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name','description','rules']


class DuelsUserForm(forms.ModelForm):
    my_hp = forms.IntegerField()
    my_army = forms.CharField(widget = forms.ChoiceField)

    class Meta:
        model = DuelUser
        fields = ['user','army','hp']