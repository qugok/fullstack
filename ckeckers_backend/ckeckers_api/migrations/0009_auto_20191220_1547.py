# Generated by Django 3.0 on 2019-12-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckeckers_api', '0008_auto_20191220_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='first_player_session_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='first_player_username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='second_player_session_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='second_player_username',
            field=models.CharField(max_length=100),
        ),
    ]
