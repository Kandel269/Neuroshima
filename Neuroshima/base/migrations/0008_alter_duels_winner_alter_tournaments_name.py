# Generated by Django 4.0.6 on 2022-08-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duels',
            name='winner',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]