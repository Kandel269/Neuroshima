from django.contrib import admin
from .models import Tournaments, Armies, Duels, DuelUser, News, Profile

# Register your models here.


admin.site.register(Tournaments)
admin.site.register(Armies)
admin.site.register(Duels)
admin.site.register(DuelUser)
admin.site.register(News)
admin.site.register(Profile)