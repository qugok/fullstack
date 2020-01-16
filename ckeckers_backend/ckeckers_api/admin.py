from django.contrib import admin

from django.contrib import admin

from .models import Option, Riddle, Game, Users

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Game)
admin.site.register(Users)

# Register your models here.
