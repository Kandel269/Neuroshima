from django.contrib.auth.models import User

from .models import Tournaments, DuelUser, Armies, Profile
from django.forms import ModelForm
from django import forms

def armies_to_list():
    armies_list = []
    armies = Armies.objects.all()
    for army in armies:
        armies_list.append( (army,str(army)) )

    return armies_list

def user_list():
    users = User.objects.all()
    return users

class TournamentForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name','description','rules','participants']


class DuelsUserForm(forms.ModelForm):
    my_hp = forms.IntegerField()
    my_army = forms.ChoiceField(choices = armies_to_list())

    class Meta:
        model = DuelUser
        fields = ['user','army','hp']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

# class ParticipantTournamentForm(forms.Form):
#     new_participant = forms.ChoiceField(choices = user_list())