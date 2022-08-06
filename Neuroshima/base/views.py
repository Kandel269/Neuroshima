from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Tournaments, Scores
from .forms import TournamentForm, DuelsForm


# Create your views here.

def loginPage(request):
    page = "login"
    login_error = None

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            login_error = "Niepoprawny login/i lub hasło!"

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            login_error = "Niepoprawny login/i lub hasło!"

    context = {'page': page, 'login_error': login_error}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Wystąpił błąd podczas rejestracji" )

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    tournaments = Tournaments.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'base/home.html', context)

def tournament(request, pk):
    tournament = Tournaments.objects.get(id=pk)
    participants = tournament.participants.all()
    scores = tournament.scores_set.all()

    # if request.method == "POST":
    #     return redirect('tournament',pk = tournament.id)

    context = {'tournament':tournament,'participants':participants,'scores':scores}
    return render(request, 'tournament/tournament.html', context)

@login_required(login_url='login')
def create_tournament(request):
    form = TournamentForm()
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            add_host = form.save(commit = False)
            add_host.host = request.user
            add_host.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'tournament/tournament_form.html', context)

def rules(request, pk):
    tournament = Tournaments.objects.get(id=pk)

    context = {'tournament':tournament}
    return render(request, 'tournament/rules.html', context)

@login_required(login_url='login')
def your_profile(request):
    actuall_user = request.user
    context = {'actuall_user':actuall_user}
    return render(request, 'profile/your_profile.html', context)

@login_required(login_url='login')
def your_tournaments(request):
    actuall_user = request.user
    tournaments = Tournaments.objects.filter(participants = actuall_user)
    context = {'actuall_user':actuall_user,'tournaments': tournaments}

    return render(request, 'profile/your_tournaments.html', context)

@login_required(login_url='login')
def add_result(request, pk):
    tournament = Tournaments.objects.get(id = pk)
    participants = tournament.participants.all()
    form = DuelsForm()
    form2 = DuelsForm()
    enemy_user_list = []

    for participant in range(len(participants)):
        if participants[participant] != request.user:
            enemy_user_list.append((str(participant), participants[participant]))
    form2.fields['user'].choices = enemy_user_list

    if request.method == "POST":
        form = DuelsForm(request.POST)
        form2 = DuelsForm(request.POST)
        if form.is_valid() and form2.is_valid():
            add_variables = form.save(commit = False)
            add_variables.user = request.user
            add_variables.tournament = tournament
            add_variables.save()
            add_variables2 = form2.save(commit = False)
            add_variables2.tournament = tournament
            form2.save()
            return redirect('home')

    context = {'form':form,'form2':form2,'tournament':tournament,'participants':participants}
    return render(request, 'tournament/add_result.html', context)