from .models import Tournaments, DuelUser, Armies
from django.forms import ModelForm
from django import forms

class TournamentForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name','description','rules']


def armies_to_list():
    armies_list = []
    armies = Armies.objects.all()
    for army in armies:
        armies_list.append( (army,str(army)) )

    return armies_list



class DuelsUserForm(forms.ModelForm):
    my_hp = forms.IntegerField()
    my_army = forms.ChoiceField(choices = armies_to_list())

    class Meta:
        model = DuelUser
        fields = ['user','army','hp']




