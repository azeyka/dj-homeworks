from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=128, verbose_name='ID игрока')

    def __str__(self):
        return self.player_id


class Game(models.Model):
    game_id = models.CharField(max_length=128, verbose_name='ID игры')
    game_creator = models.CharField(max_length=15, null=True)
    number = models.IntegerField(verbose_name='Загаданное число', null=True)
    is_finished = models.BooleanField(default=False, verbose_name='Игра завершена')
    game_winner = models.CharField(max_length=15, null=True)
    tries_number = models.IntegerField(verbose_name='Количество попыток', default=0)
    players = models.ManyToManyField(Player, through='PlayerGameInfo')

    def __str__(self):
        return self.game_id


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tries_number = models.IntegerField(verbose_name='Количество попыток', default=0)
    last_try_number = models.IntegerField(verbose_name='Последняя попытка', null=True)
    is_game_creator = models.BooleanField(default=False, verbose_name='Создатель игры')
    is_winner = models.BooleanField(default=False, verbose_name='Победитель')