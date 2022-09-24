from django.urls import path
from . import views

urlpatterns = [
    path('test/powitanie/',views.greeting_view, name='greeting_view'),
    path('test/powitanie-uzytkownika/',views.greeting_view_user, name='greeting_view_user')
]