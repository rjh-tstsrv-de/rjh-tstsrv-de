from django.contrib import admin

# Register your models here.

from rjh_rpg.models import UserChar
from rjh_rpg.models import GameState, GameScenes
from rjh_rpg.models import GamesScenesSteps
from rjh_rpg.models import HelperCounter
from rjh_rpg.models import LobbySlots
from rjh_rpg.models import Games
from rjh_rpg.models import UserCharInGames

admin.site.register(UserChar)
admin.site.register(GameState)
admin.site.register(GamesScenesSteps)
admin.site.register(GameScenes)
admin.site.register(HelperCounter)
admin.site.register(LobbySlots)
admin.site.register(Games)
admin.site.register(UserCharInGames)
