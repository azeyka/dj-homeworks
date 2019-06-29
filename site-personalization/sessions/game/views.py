from django.shortcuts import render, redirect

from .models import Player, Game, PlayerGameInfo
from .forms import SetNumberForm, CheckNumberForm
import random
import string


def show_home(request):
    # Получаем или создаем игрока
    player_id = request.session.get('player_id', f'Player-{generatetID()}')
    try:
        player = Player.objects.get(player_id=player_id)
    except Player.DoesNotExist:
        player = Player.objects.create(player_id=player_id)
        request.session['player_id'] = player_id

    # Проверяем есть ли данные о последней игре
    last_game = request.session.get('last_game_id', False)
    if last_game:
        game = Game.objects.get(game_id=last_game)
        game_info = PlayerGameInfo.objects.get(game=game, player=player)

    # Если есть, и игра завершена, то удаляем запись из сессии
    # чтобы один раз показать результаты и больше к этим данным не возвращаться
    if last_game and game.is_finished:
        del request.session['last_game_id']

    # Если данных из сессии нет, то
    elif not last_game:
        # Получаем незавершенную или создаем новую игру
        game = getOrCreateGame(player_id)

        # Добавляем игрока в игру
        is_creator = game.game_creator == player_id
        game_info = addPlayerToGame(player, game, is_creator)
        request.session['last_game_id'] = game.game_id

    if game_info.is_game_creator:
        form = SetNumberForm
    else:
        form = CheckNumberForm

    all_players = Player.objects.all().filter(playergameinfo__game=game)

    if request.method == 'POST' and not game.is_finished:
        if game_info.is_game_creator:
            form = SetNumberForm(request.POST)
            if form.is_valid():
                game.number = form.cleaned_data['number']
                game.save()
        elif game.number:
            form = CheckNumberForm(request.POST)
            if form.is_valid():
                try_number = form.cleaned_data['try_number']
                game_info.last_try_number = try_number
                game_info.tries_number += 1
                game_info.save()
                if game.number == try_number:
                    game.is_finished = True
                    game.game_winner = player_id
                    game.tries_number = game_info.tries_number
                    game.save()
        return redirect('/')

    return render(
        request,
        'home.html',
        {
            'all_players': all_players,
            'player': player,
            'game': game,
            'info': game_info,
            'form': form,
        }
    )

def generatetID():
    return f'{random.choice(string.ascii_letters)}{random.randint(0,100)}'

def getOrCreateGame(player_id):
    try:
        game = Game.objects.get(is_finished=False)
    except Game.DoesNotExist:
        game_id = f'Game-{generatetID()}'
        game = Game.objects.create(game_id=game_id, game_creator=player_id)
    return game

def addPlayerToGame(player, game, is_creator):
    return PlayerGameInfo.objects.create(
            player=player,
            game=game,
            is_game_creator=is_creator
        )