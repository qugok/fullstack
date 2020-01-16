# from django.shortcuts import render
# from rest_framework import viewsets
# # from .serializers import *
#
#
# # class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Article.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ArticlePreviewSerializer
#         return
import json

from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from . import ReadyFirstPlayerInfo
from .models import Riddle, Option, Game

from rest_framework import viewsets
from .serializers import *
from .game_logic import try_turn, get_all
from .game_table import Table
# from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import uuid
import logging
from .helpers import authenticate, create_user, exists_user, check_login, get_session_id, get_username, logout

logger = logging.getLogger('myproject.custom')


def test_working(request):
    return JsonResponse({"status": "CREATED", "csrf_token": csrf})
    table = Table()
    return HttpResponse(str(table.test()),
                        content_type='application/json')
    player_number = '1'
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)

    game = None
    try:
        if player_number == '1':
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == '2':
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR"})
    if game is None:
        return JsonResponse({"status": "ERROR"})
    return HttpResponse(get_all(game), content_type='application/json')

    return HttpResponse(str(request.user.username) + str(request.COOKIES),
                        content_type='application/json')

    table = Table()
    return HttpResponse(str(table.test()),
                        content_type='application/json')


def test_workingg(request):
    logger.info(request.POST)
    logger.info(request.GET)
    logger.info(request.content_params)
    logger.info(request.body)
    logger.info(request.COOKIES)
    table = Table()
    return HttpResponse(str(table.test()),
                        content_type='application/json')
    player_number = '1'
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})
    session_id = request.COOKIES['session_id']
    game = None
    try:
        if player_number == '1':
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == '2':
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR"})
    if game is None:
        return JsonResponse({"status": "ERROR"})
    return HttpResponse(get_all(game), content_type='application/json')

    return HttpResponse(str(request.user.username) + str(request.COOKIES),
                        content_type='application/json')

    table = Table()
    return HttpResponse(str(table.test()),
                        content_type='application/json')


def create_game(request):
    if request.method != 'POST':
        JsonResponse({"status": "ERROR"}, status=403)
    if not check_login(request):
        return JsonResponse({"status": "ERROR", "message": "YOU HAVE TO LOGIN"})

    session_id = get_session_id(request)
    username = get_username(request)
    global ReadyFirstPlayerInfo
    if ReadyFirstPlayerInfo is None:
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
        if player_number == '1':
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == '2':
            game = Game.objects.get(second_player_session_id=session_id)
    except:
        return JsonResponse({"status": "ERROR", "message": "GAME NOT FOUND"})

    ans = try_turn(game, fro, to)
    if ans:
        return JsonResponse({"status": "OK", "game_id": game.pk})
    else:
        return JsonResponse({"status": "ERROR", "game_id": game.pk})


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
        if player_number == '1':
            game = Game.objects.get(first_player_session_id=session_id)
        elif player_number == '2':
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

    session_id = get_session_id(request)
    username = get_username(request)

    data = json.loads(request.body)

    game_id = data['game_id']

    b = Game.objects.get(pk=game_id)

    message = "object deleted\nfirst player: " + b.first_player_checkers + "\nsecond player: " + b.second_player_checkers + "\ntern: " + str(
        b.turn)
    # Game.objects.filter(pk=b.pk).delete()
    b.delete()
    return render(request, "message.html", {"message": message})


def index(request):
    return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5]})


def detail(request, riddle_id):
    return render(request, "answer.html", {"riddle": get_object_or_404(Riddle, pk=riddle_id)})


def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, pk=riddle_id)
    try:
        option = riddle.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Option does not exist'})
    else:
        if option.correct:
            return render(request, "index.html", {"latest_riddles": Riddle.objects.order_by('-pub_date')[:5],
                                                  "message": "Nice! Choose another one!"})
        else:
            return render(request, 'answer.html', {'riddle': riddle, 'error_message': 'Wrong Answer!'})


def log_in(request):
    if request.method != 'POST':
        JsonResponse({"status": "ERROR"}, status=403)

    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user, session_id = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse({"status": "LOGGED IN", "username": user, "session_id": session_id})
    else:
        return JsonResponse({"status": "ERROR"}, status=401)


# def log_in1(request):
#     # logger.info(request.GET)
#     logger.info("method" + str(request.method))
#     # logger.info("get_full_path" + str(request.get_full_path()))
#     # logger.info("headers" + str(request.headers))
#     logger.info("POST" + str(request.POST))
#     logger.info("GET" + str(request.GET))
#     # logger.info("content_params" + str(request.content_params))
#     logger.info("body" + str(json.loads(request.body)))
#     # logger.info("COOKIES" + str(request.COOKIES))
#     # logger.info("META" + str(request.META))
#     # logger.info(request.REQUEST)
#     # username = request.POST['username']
#     # password = request.POST['password']
#     if request.method == 'POST':
#         return JsonResponse({"status": "ERROR"}, status=401)
#     username = request.GET['username']
#     password = request.GET['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         response = JsonResponse({"status": "LOGGED IN", 'session_id': uuid.uuid4()})
#         return response
#     else:
#         return JsonResponse({"status": "ERROR"})


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


def register1(request, username, password, email='lennon@thebeatles.com'):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    user = User.objects.create_user(username, email, password)
    if user is not None:
        user.save()
        login(request, user)
        return JsonResponse({"status": "OK", "message": "REGISTERED AND LOGGED IN"})
    else:
        return JsonResponse({"status": "ERROR"})


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all()

    serializer_class = GameSerializer
