from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .models import Tournaments, Duels, Armies, DuelUser
from .forms import TournamentForm, DuelsUserForm


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
    duels = Duels.objects.filter(tournament = tournament)
    praticipant_score_list = []
    duels_player_list = []

    for duel in duels:
        players = []
        for player in duel.users.all():
             players.append(player)
        duels_player_list.append(players)

    for participant in participants:
        counter_win = 0
        counter_draw = 0
        counter_lose = 0
        counter_big_points = 0
        counter_small_points = 0
        for duel in duels:
            for player in duel.users.all():
                if player.user == participant:
                    if duel.winner == str(participant):
                        counter_win += 1
                        counter_big_points += 1
                        counter_small_points += duel.hp_gap
                        break
                    elif duel.winner == "draw":
                        counter_draw += 1
                        counter_big_points += 0.5
                        break
                    else:
                        counter_lose += 1
                        counter_small_points -= duel.hp_gap
                        break

        praticipant_score_list.append([participant.username,counter_win,counter_draw,counter_lose,counter_big_points,counter_small_points])


    context = {'tournament':tournament,'participants':participants,'duels':duels,'praticipant_score_list':praticipant_score_list,'duels_player_list':duels_player_list}
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

    enemy_user_list = []
    form = DuelsUserForm()

    for participant in participants:
        if participant != request.user:
            enemy_user_list.append((participant.id, participant))
    form.fields['user'].choices = enemy_user_list



    if request.method == "POST":
        form = DuelsUserForm(request.POST)
        if form.is_valid():
            my_hp = form.cleaned_data.get("my_hp")
            hp = form.cleaned_data.get("hp")
            enemy = form.cleaned_data.get("user")
            army = form.cleaned_data.get("army")
            my_army = form.cleaned_data.get("my_army")

            new_duel = Duels.objects.create(tournament = tournament, winner = "", hp_gap = 0)
            if my_hp > hp:
                new_duel.hp_gap = int(my_hp) - int(hp)
                new_duel.winner = str(request.user.username)
            elif my_hp < hp:
                new_duel.hp_gap = int(hp) - int(my_hp)
                new_duel.winner = str(enemy.username)
            else:
                new_duel.hp_gap = 0
                new_duel.winner = "draw"


            my_army_obj = Armies.objects.get(name = my_army)
            owner_duel_user = DuelUser.objects.create(user = request.user, army = my_army_obj, hp = my_hp)
            enemy_duel_user = DuelUser.objects.create(user = enemy, army = army, hp = hp)

            new_duel.users.add(owner_duel_user)
            new_duel.users.add(enemy_duel_user)

            new_duel.save()

            return redirect('home')

    context = {"tournament": tournament, "form":form}
    return render(request, 'tournament/add_result.html', context)

@login_required(login_url='login')
def history_of_duels(request):
    context = {}
    return render(request, 'profile/history_of_duels.html',context)