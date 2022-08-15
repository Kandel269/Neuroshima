from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Tournaments, Scores, Duels, Armies
from .forms import TournamentForm, DuelsForm


# Create your views here.

def create_duel_list(duels):
    duel_list = []
    for duel in duels:
        if duel.enemy_id != 0:
            duel_my_enemy = Duels.objects.get(id=str(duel.enemy_id))
            duel_list.append([duel, duel_my_enemy])
        else:
            duel_my_enemy = Duels.objects.get(enemy_id=duel.id)
            duel_list.append([duel, duel_my_enemy])
    return duel_list

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

@login_required(login_url='login')
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

@login_required(login_url='login')
def update_tournmanet(request, pk):
    tournament =Tournaments.objects.get(id = pk)
    form = TournamentForm(instance = tournament)

    if request.user !=tournament.host:
        return HttpResponse('Mama ci nie pozwoliła!')

    if request.metod == "POST":
        form = TournamentForm(request.POST, instance = tournament)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'cosik', context)

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
    armies_list = ["Troglo","zombi"]
    enemy_user_list = []

    for participant in participants:
        if participant != request.user:
            enemy_user_list.append((participant.id, participant))
    form.fields['user'].choices = enemy_user_list

    if request.method == "POST":
        form = DuelsForm(request.POST)

        if form.is_valid():
            add_variables = form.save(commit = False)
            add_variables.tournament = tournament
            add_variables.enemy_id = 0
            add_variables.save()


            form_for_player = DuelsForm()
            add_variables_for_player = form_for_player.save(commit = False)
            add_variables_for_player.tournament = tournament
            add_variables_for_player.user = request.user
            add_variables_for_player.army = Armies.objects.get(name = armies_list[int(add_variables.enemy_army)-1])
            add_variables_for_player.hp = add_variables.enemy_hp
            add_variables_for_player.enemy_id = add_variables.id
            add_variables_for_player.enemy_army = add_variables.army.name
            add_variables_for_player.enemy_hp = add_variables.hp
            add_variables_for_player.save()

            return redirect('home')

    context = {'form':form,'tournament':tournament,'participants':participants}
    return render(request, 'tournament/add_result.html', context)

@login_required(login_url='login')
def history_of_duels(request):
    duels = Duels.objects.filter(user = request.user)
    duel_list = create_duel_list(duels)

    context = {'duels':duels,'duel_list':duel_list}
    return render(request, 'profile/history_of_duels.html',context)