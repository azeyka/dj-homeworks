# Generated by Django 2.1.1 on 2019-06-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_playergameinfo_is_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='game_winner',
            field=models.CharField(max_length=15, null=True),
        ),
    ]