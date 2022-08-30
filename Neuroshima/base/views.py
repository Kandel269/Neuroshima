from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



from .calculator import army_win_ratio, army_one_man_win_ratio
from .models import Tournaments, Duels, Armies, DuelUser, News, Profile
from .forms import TournamentForm, DuelsUserForm, ProfileForm

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
            new_profile = Profile(user = user, image = "profile_images/brak_foto.jpg")
            new_profile.save()
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
    news = News.objects.all().order_by('-data_create')
    context = {'news': news}
    return render(request, 'base/home.html', context)

def user_list(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'base/user_list.html', context)

def tournaments_list(request):
    tournaments = Tournaments.objects.all()
    context = {'tournaments': tournaments}
    return render(request, 'base/tournaments_list.html', context)

def tournament(request, pk):
    tournament = Tournaments.objects.get(id=pk)
    participants = tournament.participants.all()
    duels = Duels.objects.filter(tournament = tournament)
    praticipant_score_list = []


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


    context = {'tournament':tournament,'participants':participants,'duels':duels,'praticipant_score_list':praticipant_score_list}
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
    instance = actuall_user.profile

    context = {'actuall_user':actuall_user,'instance':instance}
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
    duels = Duels.objects.all()

    duels_player_list = []

    for duel in duels:
        players = []
        lock = 0
        for player in duel.users.all():
            players.append(player)
            if player.user == request.user:
                lock = 1
        if lock == 1:
            duels_player_list.append(players)

    context = {'duels_player_list': duels_player_list}
    return render(request, 'profile/history_of_duels.html',context)

def tournaments_duels(request, pk):
    tournament = Tournaments.objects.get(id=pk)
    duels = Duels.objects.filter(tournament = tournament)

    duels_player_list = []

    for duel in duels:
        players = []
        for player in duel.users.all():
             players.append(player)
        duels_player_list.append(players)

    context = {'duels_player_list':duels_player_list,'tournament':tournament}
    return render(request, 'tournament/duels.html', context)

@login_required(login_url='login')
def host_tournaments(request):
    tournaments = Tournaments.objects.filter(host = request.user)

    context = {'tournaments': tournaments}
    return render(request, "profile/host_tournament.html",context)

def tournament_statistics(request,pk):
    tournament = Tournaments.objects.get(id = pk)
    duels = Duels.objects.filter(tournament=tournament)
    armies = Armies.objects.all()

    list_score_win_ratio = army_win_ratio(duels,armies)

    context = {'tournament':tournament,'armies':armies,'list_score_win_ratio':list_score_win_ratio}
    return render(request, 'tournament/statistics.html', context)

def profile_statistics(request):
    all_duels = Duels.objects.all()
    duels = []
    for duel in all_duels:
        lock = 0
        for player in duel.users.all():
            if request.user == player.user:
                if lock == 0:
                    duels.append(duel)
                    lock += 1

    armies = Armies.objects.all()

    list_score_win_ratio = army_one_man_win_ratio(duels, armies,str(request.user))

    context = {'armies':armies,'list_score_win_ratio':list_score_win_ratio}
    return render(request, 'profile/profile_statistics.html', context)

@login_required(login_url='login')
def profile_settings(request):
    current_user = request.user
    current_profile = current_user.profile
    form = ProfileForm(instance = current_profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = current_profile)
        if form.is_valid():
            form.save()

            return redirect('home')
    context = {'form':form}
    return render(request, 'profile/profile_settings.html',context)


@login_required(login_url='login')
def create_tournament(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            add_host = form.save(commit = False)
            add_host.host = request.user
            add_host.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'tournament/tournament_form.html', context)

def TournamentSearchView(request):
    query = request.POST['home_search']
    category = request.POST['home_select']

    if category[0:3] == "tou":
        if category == "tournament_name":
            tournaments = Tournaments.objects.filter(name__icontains=query)
        else:
            try:
                get_user = User.objects.get(username = query)
                user_id = get_user.id
                tournaments = Tournaments.objects.filter(host = user_id)
            except:
                tournaments = ""
    else:
    #     jeszce nie opracowane
        tournaments = Tournaments.objects.all()

    query_len = len(tournaments)

    context = {'query':query,'tournaments':tournaments,'query_len':query_len}
    return render(request, 'base/search.html', context)

@login_required(login_url='login')
def delete_tournament(request, pk):
    tournament = Tournaments.objects.get(id = pk)

    if request.user != tournament.host:
        return HttpResponse('Nie masz zgody od rodziców na przebywanie w tym miejscu')

    if request.method == "POST":
        tournament.delete()
        return redirect('home')

    context = {'tournament':tournament}
    return render(request, 'tournament/delete_tournament.html',context)

@login_required(login_url='login')
def tournament_settings(request, pk):
    tournament = Tournaments.objects.get(id = pk)

    if request.user != tournament.host:
        return HttpResponse('Nie masz zgody od rodziców na przebywanie w tym miejscu')

    context = {'tournament':tournament}
    return render(request, "tournament/tournament_settings.html", context)

@login_required(login_url='login')
def update_tournmanet(request, pk):
    tournament =Tournaments.objects.get(id = pk)
    form = TournamentForm(instance = tournament)

    if request.user != tournament.host:
        return HttpResponse('Mama ci nie pozwoliła!')

    if request.method == "POST":
        form = TournamentForm(request.POST, instance = tournament)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form,'tournament':tournament}
    return render(request, 'tournament/tournament_edit.html', context)




