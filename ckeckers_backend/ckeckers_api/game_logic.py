from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
# from . import ReadyFirstPlayerSessionId
from .models import Riddle, Option, Game

from rest_framework import viewsets
from .serializers import *
import logging

logger = logging.getLogger('myproject.custom')

from .game_table import Table

def try_turn(game, fro:str, to):
    fro = tuple(map(int, fro.split(':', maxsplit=1)))
    to = tuple(map(int, to.split(':', maxsplit=1)))
    table = Table(game.size, game.turn)
    table.deserialize(game.first_player_checkers, game.second_player_checkers)
    logger.info('\n'+str(table))
    ans = table.go(fro, to)
    if not ans:
        return False

    f, s = table.serialize()
    logger.info(str(table))
    game.first_player_checkers = f
    game.second_player_checkers = s

    game.turn = table.turn

    game.save()
    return True


def get_score(game, fro, to):
    table = Table(game.size, turn=game.turn)
    table.deserialize(game.first_player_checkers, game.second_player_checkers)
    return table.get_score()


def get_all(game):
    table = Table(game.size, turn=game.turn)
    logger.info(str(table.serialize()))
    table.deserialize(game.first_player_checkers, game.second_player_checkers)
    logger.info('\n'+game.first_player_checkers +'\n'+ game.second_player_checkers)
    return str(table.turn) + '\n\n' + '\n'.join([str((p.x, p.y, p.player)) + str(table.can_go((p.x, p.y))) for line in table.table for p in line])



