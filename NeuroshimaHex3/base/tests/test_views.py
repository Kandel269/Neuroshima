from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

class TestCreateTournament(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username= "Noob", password="Noobpassword")
        self.test_user.save()
        self.client = Client()

    def test_user_create_tournament_not_authenticated(self):
        response = self.client.get('/twoj-profil/stworz-turniej/')
        self.assertEquals(response.status_code, 302)

    def test_user_authenticaed(self):
        login = self.client.login(username= "Noob", password="Noobpassword")
        response = self.client.get('/twoj-profil/stworz-turniej/')
        self.assertEquals(response.status_code, 200)