from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Armies(models.Model):
    name = models.CharField(max_length=255)
    # tiles = models.ExpressionList

    def __str__(self):
        return self.name

class Tournaments(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 200)
    # edition =
    description = models.TextField(null = True, blank = True)
    rules = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name = 'participants', blank = True)
    # mode = models.
    # rounds = models

    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Scores(models.Model):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True)
    game = models.ForeignKey(Tournaments, on_delete= models.CASCADE)
    big_points = models.IntegerField()
    small_points = models.IntegerField()
    win_count = models.IntegerField()
    draw_count = models.IntegerField()
    lose_count = models.IntegerField()

class Duels(models.Model):
    tournament = models.ForeignKey(Tournaments, on_delete= models.SET_NULL, null = True, blank = True)
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
    army = models.ForeignKey(Armies, on_delete= models.SET_NULL, null = True)
    hp = models.IntegerField()
    enemy_id = models.IntegerField(null = True, blank = True)
    enemy_army = models.CharField(max_length=255, choices = [("1",'Troglo'),('2',"zombi")])
    enemy_hp = models.IntegerField()
