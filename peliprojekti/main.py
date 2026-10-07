import classes
import functions
import objects




    

#jobs_available = (models.Job("myyjä"), models.Job("sairaanhoitaja"), models.Job("koodari"), models.Job("kuljettaja"), 
#models.Job("siivoja"), models.Job("kokki"), models.Job("kielenopettaja"), models.Job("puutarhuri"))



# Ohjelman startti ja päävalikko
player = functions.run_game()


# Uusi peli ja pelin prosessi

functions.main_menu(player)
functions.new_game()
functions.game_loop(player)        
        

    

