from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('szukaj/', views.TournamentSearchView, name = 'search' ),

    path('logowanie/', views.loginPage, name = 'login'),
    path('rejestracja/', views.registerPage, name = 'register'),
    path('wylogowanie/', views.logoutUser, name = 'logout'),

    path('turniej/<str:pk>/', views.tournament, name = 'tournament'),
    path('turniej/<str:pk>/zasady-turnieju/', views.rules, name = 'rules'),
    path('turniej/<str:pk>/dodaj-wynik/', views.add_result ,name = 'duel'),
    path('turniej/<str:pk>/historia-pojedynków/', views.tournaments_duels ,name = 'history_of_duels'),
    path('turniej/<str:pk>/statystyki/', views.tournament_statistics ,name = 'tournament_statistics'),
    path('turniej/<str:pk>/usuń-turniej/', views.delete_tournament ,name = 'delete_tournament'),
    path('turniej/<str:pk>/ustawienia-turnieju/', views.tournament_settings ,name = 'tournament_settings'),

    path('twoj-profil/', views.your_profile, name = 'your_profile'),
    path('twoj-profil/twoje-turnieje/', views.your_tournaments, name ='your_tournaments'),
    path('twoj-profil/gospodarz-turniejów/', views.host_tournaments, name ='host_tournaments'),
    path('twoj-profil/stworz-turniej/', views.create_tournament, name='create_tournament'),
    path('twoj-profil/historia-pojedynków/', views.history_of_duels, name='history_of_duels'),
    path('twoj-profil/statystyki/', views.profile_statistics, name='profile_statistics'),

]
