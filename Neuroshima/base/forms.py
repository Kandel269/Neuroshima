from .models import Tournament
from django.forms import ModelForm

class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
