# Generated by Django 4.0.6 on 2022-09-20 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa turnieju', max_length=50)),
                ('website', models.URLField(help_text='strona_turnieju')),
                ('email', models.EmailField(help_text='e-mail do tworcy turnieju', max_length=254)),
            ],
        ),
    ]