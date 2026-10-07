import classes

home_loc = classes.Room("Koti", "Oma vuokraasunto")
TE_room = classes.Room("TE-toimisto", "Tästä haet töitä")
store = classes.Room("Kauppa", "\nIhan normaali kauppa, " \
"josta voi ostaa ruokaa ja muuta ")
lib = classes.Room("Kirjasto", "Tässä voi hoitaa asiota rauhassa")





cv_item = classes.Item("cv-lomake", 0.1)
# HOME STUFF
home_loc.add_item(cv_item)
    
home_loc.actions = ["syödä", "nukkua"]

#
TE_room.exits = {"koti": home_loc}
store.exits = {"koti": home_loc}
home_loc.exits = {"te-toimisto": TE_room, "kirjasto": lib, "kauppa": store}