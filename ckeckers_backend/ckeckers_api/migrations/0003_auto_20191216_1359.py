# Generated by Django 3.0 on 2019-12-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckeckers_api', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='first_player_session_id',
            field=models.CharField(default='qwe', max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='second_player_session_id',
            field=models.CharField(default='qwe', max_length=100),
        ),
    ]
