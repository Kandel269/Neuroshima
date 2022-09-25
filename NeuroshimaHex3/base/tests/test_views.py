from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Tournaments


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

class TestCreateTournamentView(TestCase):
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

class TestDeleteTournamentView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="Noob",password="Noobpassword")
        self.test_user.save()
        self.wrong_user = User.objects.create_user(username="Newbie",password="Newbiepassword")
        self.wrong_user.save()

        self.client = Client()
        self.obj = Tournaments(host = self.test_user, name = "NoobTournament")
        self.obj.save()

    def test_wrong_user_delete_tournament(self):
        login = self.client.login(username="Newbie",password="Newbiepassword")
        test_id = self.obj.id
        response = self.client.get(f'/turniej/{test_id}/usun-turniej/')
        self.assertEquals(response.status_code, 200)

    def test_user_delete_tournament(self):
        login = self.client.login(username="Noob",password="Noobpassword")
        test_id = self.obj.id
        response = self.client.get(f'/turniej/{test_id}/usun-turniej/')
        self.assertEquals(response.status_code, 200)

    def test_anonymus_user_delete_tournament(self):
        test_id = self.obj.id
        response = self.client.get(f'/turniej/{test_id}/usun-turniej/')
        self.assertEquals(response.status_code, 302)