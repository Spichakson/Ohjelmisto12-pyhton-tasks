import functions






# Ohjelman startti ja päävalikko
player, rooms_dict, items_dict = functions.run_game()
active_player = functions.main_menu(rooms_dict, items_dict, player)


# Uusi peli ja pelin prosessi
if active_player:
    functions.game_loop(active_player)
