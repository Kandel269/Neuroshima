from django.db import models

class NewTournament(models.Model):
    name = models.CharField(max_length=50, help_text='Nazwa turnieju')
    website = models.URLField(help_text='strona_turnieju')
    email = models.EmailField(help_text='e-mail do tworcy turnieju')

    def __str__(self):
        return self.name