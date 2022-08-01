from .models import Tournaments
from django.forms import ModelForm

class TournamentForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = '__all__'
