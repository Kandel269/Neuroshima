from django.test import TestCase, Client

# Create your tests here.
from ..models import NewTournament
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from ..views import greeting_view_user

class TestNewTournament(TestCase):
    def setUp(self):
        self.p = NewTournament(name = 'Packt',website = 'www.packt.com',email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, NewTournament)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")

class TestGreetingView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/powitanie/')
        self.assertEquals(response.status_code, 200)

# class TestLoggedInGreetingView(TestCase):
#     def setUp(self):
#         test_user = User.objects.create_user(username='testuser',password='test@#628password')
#         test_user.save()
#         self.client = Client()
#
#     def test_user_greeting_not_authenticated(self):
#         response = self.client.get('/test/powitanie-uzytkownika/')
#         self.assertEquals(response.status_code, 302)
#
#     def test_user_authenticated(self):
#         login = self.client.login(username='testuser',password='test@#628password')
#         response = self.client.get('/test/powitanie-uzytkownika/')
#         self.assertEquals(response.status_code, 200)

class TestLoggedInGreetingView(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_greeting_not_authenticated(self):
        request = self.factory.get('/test/powitanie-uzytkownika/')
        request.user = AnonymousUser()
        response = greeting_view_user(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/test/powitanie-uzytkownika/')
        request.user = self.test_user
        response = greeting_view_user(request)
        self.assertEquals(response.status_code, 200)

