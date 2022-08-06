from .models import Tournaments, Duels
from django.forms import ModelForm

class TournamentForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name','description','rules']


class DuelsForm(ModelForm):
    class Meta:
        model = Duels
        fields = ['user','army','hp','enemy']
