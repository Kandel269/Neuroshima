from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    path('logowanie/', views.loginPage, name = 'login'),
    path('rejestracja/', views.registerPage, name = 'register'),
    path('wylogowanie/', views.logoutUser, name = 'logout'),

    path('turniej/<str:pk>/', views.tournament, name = 'tournament'),
    path('stworz-turniej/', views.create_tournament, name = 'create_tournament'),
    path('zasady-turnieju/<str:pk>/', views.rules, name = 'rules'),

    path('twoj-profil/', views.your_profile, name = 'your_profile'),
    path('twoj-profil/twoje-turnieje/', views.your_tournaments, name ='your_tournaments'),

]
