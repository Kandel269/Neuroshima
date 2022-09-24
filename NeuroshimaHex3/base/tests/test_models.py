from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta, datetime
import mock

from ..models import Tournaments, Armies, News


class TestArmies(TestCase):
    def setUp(self):
        self.obj = Armies(name = "Grenadierzy")

    def test_create_army(self):
        self.assertIsInstance(self.obj, Armies)

    def test_str_representation(self):
        self.assertEquals(str(self.obj), "Grenadierzy")

class TestTournament(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser',password='testmypassword')
        self.test_user.save()
        self.obj = Tournaments(host = self.test_user, name="The_best",description = "lorem ipsum",rules="lorem ipsum lorem")
        self.obj.host = self.test_user
        self.obj.save()
        self.participant1 = self.obj.participants.create(username = 'Zbyszek', password='zbyszekpassword')
        self.participant1.save()

    def test_create_tournament(self):
        self.assertIsInstance(self.obj, Tournaments)

    def test_str_representation(self):
        self.assertEquals(str(self.obj), "The_best")

    def test_host_name(self):
        self.assertEquals(str(self.obj.host.username), "testuser")

    def test_participant(self):
        self.assertEquals(self.obj.participants.get(pk = self.participant1.pk), self.participant1)

class TestNews(TestCase):
    def setUp(self):
        self.yesterday = datetime.now() - timedelta(days = 1)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = self.yesterday
            self.obj = News(title = "good_title", description="lorem ipsum")
            self.obj.save()

    def test_data_create(self):
       self.assertEquals(self.obj.data_create, self.yesterday)

    def test_str_representation(self):
        self.assertEquals(str(self.obj), "good_title")



