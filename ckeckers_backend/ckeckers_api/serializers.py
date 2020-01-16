from rest_framework import serializers
from ckeckers_api.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'id',
            'size',
            'first_player_checkers',
            'first_player_session_id',
            'second_player_checkers',
            'second_player_session_id',
            'turn',
            'url',
        ]
