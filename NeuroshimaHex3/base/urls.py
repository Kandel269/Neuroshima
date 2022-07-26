from django.urls import path
from . import views
from .api_views import first_api_view, AllNews, AllArmies, Login


urlpatterns = [
    path('', views.home, name = 'home'),
    path('lista-turniejow', views.tournaments_list, name = 'tournaments_list'),
    path('szukaj/', views.TournamentSearchView, name = 'search' ),
    path('lista-użytkownikow', views.user_list, name='user_list'),

    path('logowanie/', views.loginPage, name = 'login'),
    path('rejestracja/', views.registerPage, name = 'register'),
    path('wylogowanie/', views.logoutUser, name = 'logout'),

    path('turniej/<str:pk>/', views.tournament, name = 'tournament'),
    path('turniej/<str:pk>/zasady-turnieju/', views.rules, name = 'rules'),
    path('turniej/<str:pk>/dodaj-wynik/', views.add_result ,name = 'duel'),
    path('turniej/<str:pk>/historia-pojedynkow/', views.tournaments_duels ,name = 'history_of_duels'),
    path('turniej/<str:pk>/statystyki/', views.tournament_statistics ,name = 'tournament_statistics'),
    path('turniej/<str:pk>/usun-turniej/', views.delete_tournament ,name = 'delete_tournament'),
    path('turniej/<str:pk>/ustawienia-turnieju/', views.tournament_settings ,name = 'tournament_settings'),
    path('turniej/<str:pk>/ustawienia-turnieju/edytu-turniej', views.update_tournmanet ,name = 'tournament_edit'),

    path('twoj-profil/', views.your_profile, name = 'your_profile'),
    path('twoj-profil/twoje-turnieje/', views.your_tournaments, name ='your_tournaments'),
    path('twoj-profil/gospodarz-turniejow/', views.host_tournaments, name ='host_tournaments'),
    path('twoj-profil/stworz-turniej/', views.create_tournament, name='create_tournament'),
    path('twoj-profil/historia-pojedynków/', views.history_of_duels, name='history_of_duels'),
    path('twoj-profil/statystyki/', views.profile_statistics, name='profile_statistics'),
    path('twoj-profil/ustawienia/', views.profile_settings, name='profile_settings'),

    ## rest- api
    path('api/login', Login.as_view(), name='api_login'),
    path('api/pierwszy-widok-api/', first_api_view, name = 'first_api'),
    path('api/wszystkie-wiadomosci/', AllNews.as_view(), name = 'all_news'),
    path('api/wszystkie-armie/', AllArmies.as_view(), name = 'all_armies'),


]
