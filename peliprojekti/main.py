import functions


player, rooms_dict, items_dict = functions.run_game()


result = functions.main_menu(rooms_dict, items_dict, player)


if result:
    active_player, rooms_dict, items_dict = result
    functions.game_loop(active_player)