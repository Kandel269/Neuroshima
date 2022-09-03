from django.contrib.auth.models import User
from django.db import models
from base.models import Tournaments
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic,on_delete = models.SET_NULL, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    tournament = models.OneToOneField(Tournaments, null = True, blank = True, on_delete= models.CASCADE)
    data_create =  models.DateTimeField(auto_now_add = True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Messages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    data_create =  models.DateTimeField(auto_now_add = True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]