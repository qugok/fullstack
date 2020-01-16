"""ckeckers_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from rest_framework.routers import DefaultRouter
# from .views import *
# http://0.0.0.0:25001/my_api/command=check_for_creation&session_id=efc049da-3a0f-4a7e-9515-039a5d2ceb52

# router = DefaultRouter()
# router.register(r'articles', ArticleViewSet)


# urlpatterns = router.urls

# from django.conf.urls import url
#
# from . import views
#
# # app_name = 'riddles'
# efc049da-3a0f-4a7e-9515-039a5d2ceb51
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from . import views
from ckeckers_backend.settings import DEBUG
from django.views.decorators.csrf import csrf_exempt


create_game = r'create_game'
check_for_creation = r'check_for_creation'
# make_turn = r'make_turn\?player_number=(?P<player_number>\d)&from=(?P<fro>.+)&to=(?P<to>.+)'
make_turn = r'make_turn'
# can_make_tern = r'can_make_turn\?player_number=(?P<player_number>\d)'
can_make_turn = r'can_make_turn'
# get_all_table = r'get_all_table\?player_number=(?P<player_number>\d)'
get_all_table = r'get_all_table'
# login = r'login\?username=(?P<username>\w+)&password=(?P<password>.+)'
login1 = r'login'
logout = r'logout'
# register = r'register\?username=(?P<username>\w+)&password=(?P<password>.+)&email=(?P<email>.+)'
register = r'register'


urlpatterns = [
    url(create_game, csrf_exempt(views.create_game), name='create_game'),
    url(check_for_creation, csrf_exempt(views.check_for_creation), name='check_for_creation'),
    url(make_turn, csrf_exempt(views.make_turn), name='make_turn'),
    url(register, csrf_exempt(views.register), name='register'),
    url(get_all_table, csrf_exempt(views.get_all_table), name='get_all_table'),
    # url(login, views.log_in, name='login'),
    url(login1, csrf_exempt(views.log_in), name='login1'),
    url(logout, csrf_exempt(views.logout_view), name='logout'),
    url(can_make_turn, csrf_exempt(views.can_make_turn), name='can_make_turn'),
]

if DEBUG:
    detail = r'^(?P<riddle_id>[0-9]+)/$'
    answer = r'^(?P<riddle_id>[0-9]+)/answer/$'
    delete_game = r'^command=delete_game&game_id=(?P<game_id>[0-9]+)$'

    urlpatterns.extend([
        url(r'^$', views.index, name='index'),
        url(detail, views.detail, name='detail'),
        # url("test", views.test_working, name='test'),
        url("testt", views.test_workingg, name='testt'),
        url(answer, views.answer, name='answer'),
        url(delete_game, views.delete_game, name='delete_game'),
    ])

    router = DefaultRouter()
    router.register(r'articles', views.GameViewSet)

    urlpatterns.extend(router.urls)
