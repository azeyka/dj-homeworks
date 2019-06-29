from django.forms import BaseInlineFormSet

from django.contrib import admin
from .models import Player, Game, PlayerGameInfo


class GameInfoInlineFormset(BaseInlineFormSet):
  pass


class GameInfoInline(admin.TabularInline):
  model = PlayerGameInfo
  formset = GameInfoInlineFormset


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
  inlines = [GameInfoInline]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  pass

@admin.register(PlayerGameInfo)
class PlayerGameInfoAdmin(admin.ModelAdmin):
  pass

