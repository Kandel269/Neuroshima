# Generated by Django 4.0.6 on 2022-09-03 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_topic_alter_room_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.topic'),
        ),
    ]
