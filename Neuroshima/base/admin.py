from django.contrib import admin
from .models import Tournaments, Scores, Armies, Duels, DuelUser

# Register your models here.


admin.site.register(Tournaments)
admin.site.register(Scores)
admin.site.register(Armies)
admin.site.register(Duels)
admin.site.register(DuelUser)