# Generated by Django 4.0.6 on 2022-08-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
