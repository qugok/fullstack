from django.db import models

class Game(models.Model):
    size = models.IntegerField(default=8)
    first_player_checkers = models.CharField(max_length=100, default="0:0@0#0:2@0#1:1@0#2:0@0#2:2@0#3:1@0#4:0@0#4:2@0#5:1@0#6:0@0#6:2@0#7:1@0")
    first_player_username = models.CharField(max_length=100)
    first_player_session_id = models.CharField(max_length=100)
    second_player_checkers = models.CharField(max_length=100, default="0:6@0#1:5@0#1:7@0#2:6@0#3:5@0#3:7@0#4:6@0#5:5@0#5:7@0#6:6@0#7:5@0#7:7@0")
    second_player_username = models.CharField(max_length=100)
    second_player_session_id = models.CharField(max_length=100)
    turn = models.IntegerField(default=1) # 0 - game over 1 - first tern, 2- second tern

    class Meta:
        ordering = ('first_player_username',)

class Users(models.Model):
    username = models.CharField(max_length=100)
    sha256_password = models.CharField(max_length=100)
    user_actual_session_id = models.CharField(max_length=100)