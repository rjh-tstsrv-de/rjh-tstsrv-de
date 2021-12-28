from rjh_rpg.models import GameScenes, Games, UserCharInGames
from channels.db import database_sync_to_async
import random

@database_sync_to_async
def db_set_game_id_to_finished(game_id):
    return Games.objects.filter(id=game_id).update(game_finished=True)

@database_sync_to_async
def db_get_is_game_id_finished(game_id):
    return Games.objects.get(id=game_id).game_finished


@database_sync_to_async
def db_get_game_log(game_id):
    return str(Games.objects.get(id=game_id).game_log)

@database_sync_to_async
def db_expand_game_log(game_id, text_to_add):
    game_obj = Games.objects.get(id=game_id)
    game_log_now = str(game_obj.game_log)
    game_log_new = game_log_now + str(text_to_add)
    game_obj.game_log = game_log_new
    game_obj.save()

@database_sync_to_async
def db_get_round_state(game_id):
    return Games.objects.get(id=game_id).round_state

@database_sync_to_async
def db_set_round_state(game_id, new_round_state):
    return Games.objects.filter(id=game_id).update(round_state=new_round_state)

@database_sync_to_async
def db_get_is_round_state_locked(game_id):
    return bool(Games.objects.get(id=game_id).round_state_locked)

@database_sync_to_async
def db_set_round_state_locked(game_id, new_round_state_locked):
    return Games.objects.filter(id=game_id).update(round_state=bool(new_round_state_locked))


@database_sync_to_async
def db_increase_round_counter(game_id):
    return Games.objects.filter(id=game_id).update(round_counter=(int(Games.objects.get(id=game_id).round_counter)+1))

@database_sync_to_async
def db_get_round_counter(game_id):
    return int(Games.objects.get(id=game_id).round_counter)


@database_sync_to_async
def db_get_enemy_name(game_id):
    game_scene_id = Games.objects.get(id=game_id).game_scene_id
    return str(GameScenes.objects.get(name=game_scene_id).enemy_name)

@database_sync_to_async
def db_get_enemy_ap(game_id):
    game_scene_id = Games.objects.get(id=game_id).game_scene_id
    return int(GameScenes.objects.get(name=game_scene_id).enemy_ap)


@database_sync_to_async
def db_get_user_char_in_game_list(game_id):
    user_chars_in_game = UserCharInGames.objects.filter(game_id=game_id)
    user_char_in_game_list = [] 
    for user_char in user_chars_in_game:
        user_char_in_game_list.append(user_char.user_char_id)
    return user_char_in_game_list

@database_sync_to_async
def db_get_random_alive_user_char_in_games_id(game_id):
    alive_user_chars = UserCharInGames.objects.filter(game_id=game_id, current_hp__gte = 0)
    random_alive_user_char = random.choice(alive_user_chars)
    return random_alive_user_char.id

@database_sync_to_async
def db_give_dmg_to_user_char(user_char_in_games_id, ap_to_deliver):
    last_hp = UserCharInGames.objects.get(id=user_char_in_games_id).current_hp
    new_hp = last_hp - int(ap_to_deliver)
    if new_hp < 0:
        new_hp = 0
    UserCharInGames.objects.filter(id=user_char_in_games_id).update(current_hp=new_hp)
    dmg_taken = ap_to_deliver
    return (last_hp, new_hp, dmg_taken)
    
@database_sync_to_async
def db_get_char_name_of_user_char_in_games_id(user_char_in_games_id):
    char_name = UserCharInGames.objects.get(id=user_char_in_games_id).user_char_id
    return str(char_name)


