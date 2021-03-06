# Generated by Django 3.0 on 2019-12-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckeckers_api', '0003_auto_20191216_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='first_player_username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='second_player_username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='first_player_checkers',
            field=models.CharField(default='0:0@0#0:2@0%1:1@0%2:0@0#2:2@0%3:1@0%4:0@0#4:2@0%5:1@0%6:0@0#6:2@0%7:1@0', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='first_player_session_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='second_player_checkers',
            field=models.CharField(default='0:6@0%1:5@0#1:7@0%2:6@0%3:5@0#3:7@0%4:6@0%5:5@0#5:7@0%6:6@0%7:5@0#7:7@0', max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='second_player_session_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='turn',
            field=models.IntegerField(default=1),
        ),
    ]
