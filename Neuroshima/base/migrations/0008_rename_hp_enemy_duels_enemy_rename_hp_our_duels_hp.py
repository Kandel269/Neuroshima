# Generated by Django 4.0.6 on 2022-08-06 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_rename_hp1_duels_hp_enemy_rename_hp2_duels_hp_our'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duels',
            old_name='hp_enemy',
            new_name='enemy',
        ),
        migrations.RenameField(
            model_name='duels',
            old_name='hp_our',
            new_name='hp',
        ),
    ]