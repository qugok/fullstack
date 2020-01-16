import json

from django.shortcuts import render

from rest_framework import viewsets
from .serializers import *
from .game_logic import try_turn
from .game_table import Table
from django.http import JsonResponse
import logging
from .helpers import authenticate, create_user, exists_user, check_login, get_session_id, get_username, logout

logger = logging.getLogger('myproject.custom')

def create_game(request):
    if request.method != 'POST':
        JsonResponse({"status": "ERROR"}, status=403)
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)
    global ReadyFirstPlayerInfo
    if ReadyFirstPlayerInfo is None or ReadyFirstPlayerInfo == (session_id, username):
        ReadyFirstPlayerInfo = (session_id, username)
        return JsonResponse({"status": "PENDING"})
    new_game = Game(first_player_session_id=ReadyFirstPlayerInfo[0], first_player_username=ReadyFirstPlayerInfo[1],
                    second_player_session_id=session_id, second_player_username=username)
    new_game.save()
    ReadyFirstPlayerInfo = None
    return JsonResponse({"status": "CREATED", "game_id": new_game.pk, "player_number": 2})


def check_for_creation(request):
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)

    if ReadyFirstPlayerInfo == (session_id, username):
        return JsonResponse({"status": "PENDING"})
    elif Game.objects.filter(first_player_session_id=session_id).exists():
        game_id = Game.objects.get(first_player_session_id=session_id).pk
        return JsonResponse({"status": "CREATED", "game_id": game_id, "player_number": 1})
    else:
        return JsonResponse({"status": "ERROR"})


def make_turn(request):
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)

    data = json.loads(request.body)

    player_number = data['player_number']
    fro = data['fro']
    to = data['to']

    game = None
    try:
        if player_number == 1:
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == 2:
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR", "message": "GAME NOT FOUND"})

    ans = try_turn(game, fro, to)
    if ans:
        return JsonResponse({"status": "OK", "game_id": game.pk})
    else:
        return JsonResponse({"status": "FAIL", "game_id": game.pk})


def choose_game(request, game_id):
    pass


def get_all_table(request):
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})


    session_id = get_session_id(request)
    username = get_username(request)

    data = json.loads(request.body)

    player_number = data['player_number']

    game = None
    try:
        if player_number == 1:
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == 2:
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR"})
    # return JsonResponse({"status": "OK", "game_id": game.pk, "first_player": game.first_player_checkers,
    #                      "second_player": game.second_player_checkers, "turn": game.turn})

    table = Table(game.size, game.turn)
    table.deserialize(game.first_player_checkers, game.second_player_checkers)
    return JsonResponse({"status": "OK", "table": table.to_json_like_with_table()})


def can_make_turn(request):
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)

    data = json.loads(request.body)

    player_number = data['player_number']

    game = None
    try:
        if player_number == '1':
            game = Game.objects.get(first_player_session_id=session_id)
        else:
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR"})
    if game.turn == 0:
        return JsonResponse({"status": "FINISHED", "game_id": "" + str(game.pk) + ""})
    elif str(game.turn) == player_number:
        return JsonResponse({"status": "OK", "game_id": game.pk})
    else:
        return JsonResponse({"status": "PENDING", "game_id": game.pk})


def delete_game(request):

    # session_id = get_session_id(request)
    # username = get_username(request)

    data = json.loads(request.body)

    game_id = data['game_id']

    b = Game.objects.get(pk=game_id)

    message = "object deleted\nfirst player: " + b.first_player_checkers + "\nsecond player: " + b.second_player_checkers + "\ntern: " + str(b.turn)
    b.delete()
    return render(request, "message.html", {"message": message})



def is_logged_in(request):
    if check_login(request):
        return JsonResponse({"status": "OK", "message": "YOU ARE LOGGED IN"})
    return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})


def log_in(request):
    if request.method != 'POST':
        JsonResponse({"status": "ERROR"})

    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user, session_id = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({"status": "LOGGED IN", "username": user, "session_id": session_id})
    else:
        return JsonResponse({"status": "ERROR"})


def logout_view(request):
    logger.info("body" + str(request.body))
    logout(request)
    return JsonResponse({"status": "OK", "message": "YOU ARE NOT LOGGED IN"})


def register(request):
    if request.method != 'POST':
        JsonResponse({"status": "ERROR"}, status=403)

    data = json.loads(request.body)

    username = data['username']
    password = data['password']

    if exists_user(username):
        return JsonResponse({"status": "ERROR"})

    user, session_id = create_user(username, password)

    if user is not None:
        return JsonResponse({"status": "REGISTERED AND LOGGED IN", "username": username, "session_id": session_id})
    else:
        return JsonResponse({"status": "ERROR"}, status=401)


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()

    serializer_class = GameSerializer
