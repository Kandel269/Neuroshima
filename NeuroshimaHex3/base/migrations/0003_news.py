# Generated by Django 4.0.6 on 2022-08-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_duels_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descrition', models.TextField()),
                ('data_create', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]