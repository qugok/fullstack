from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from . import views
from ckeckers_backend.settings import DEBUG
from django.views.decorators.csrf import csrf_exempt


create_game = r'create_game'
check_for_creation = r'check_for_creation'
make_turn = r'make_turn'
is_logged_in = r'is_logged_in'
can_make_turn = r'can_make_turn'
get_all_table = r'get_all_table'
login = r'login'
logout = r'logout'
register = r'register'


urlpatterns = [
    url(create_game, csrf_exempt(views.create_game), name='create_game'),
    url(check_for_creation, csrf_exempt(views.check_for_creation), name='check_for_creation'),
    url(make_turn, csrf_exempt(views.make_turn), name='make_turn'),
    url(register, csrf_exempt(views.register), name='register'),
    url(get_all_table, csrf_exempt(views.get_all_table), name='get_all_table'),
    url(login, csrf_exempt(views.log_in), name='login'),
    url(is_logged_in, csrf_exempt(views.is_logged_in), name='is_logged_in'),
    url(logout, csrf_exempt(views.logout_view), name='logout'),
    url(can_make_turn, csrf_exempt(views.can_make_turn), name='can_make_turn'),
]

if DEBUG:
    detail = r'^(?P<riddle_id>[0-9]+)/$'
    answer = r'^(?P<riddle_id>[0-9]+)/answer/$'
    delete_game = r'^command=delete_game&game_id=(?P<game_id>[0-9]+)$'

    urlpatterns.extend([
        url(delete_game, views.delete_game, name='delete_game'),
    ])

    router = DefaultRouter()
    router.register(r'Games', views.GameViewSet)

    urlpatterns.extend(router.urls)
