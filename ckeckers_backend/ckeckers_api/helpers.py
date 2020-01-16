import json
import uuid

from .models import Users

import logging
logger = logging.getLogger('myproject.custom')

def authenticate(username, password):
    if not Users.objects.filter(username=username, sha256_password=password).exists():
        return None, None
    user = Users.objects.get(username=username)
    user.user_actual_session_id = uuid.uuid4()
    user.save()
    return username, user.user_actual_session_id


def create_user(username, password):
    if Users.objects.filter(username=username).exists():
        return None, None
    user = Users(username=username, sha256_password=password, user_actual_session_id=uuid.uuid4())
    user.save()
    return user.username, user.user_actual_session_id


def exists_user(username):
    return Users.objects.filter(username=username).exists()


def get_session_id(request):
    try:
        return json.loads(request.body)['session_id']
    except:
        return None


def get_username(request):
    try:
        return json.loads(request.body)['username']
    except:
        return None


def check_login(request):
    session_id = get_session_id(request)
    logger.info(session_id)
    if session_id is None or session_id == 'None':
        return False
    username = get_username(request)
    logger.info(username)
    if username is None:
        return False
    logger.info(Users.objects.filter(username=username, user_actual_session_id=session_id).exists())
    if Users.objects.filter(username=username, user_actual_session_id=session_id).exists():
        return True
    return False


def logout(request):
    username = get_username(request)
    user = Users.objects.get(username=username)
    user.user_actual_session_id = 'None'
    user.save()
    return