class Elevator:
    def __init__(self, bot_f, top_f):
        self.bot_f = bot_f
        self.top_f = top_f
        self.current_floor = bot_f
        

    def floor_up(self):
         self.current_floor += 1
         return print(f"The elevator is on the {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        return print(f"The elevator is on the {self.current_floor}")
    
    def go_to_floor(self, f_number):
        
        if f_number > self.top_f:
            f_number = self.top_f
        elif f_number < self.bot_f:
            f_number = self.bot_f

        print(f"The elevator is moving to the floor {f_number}")

        while f_number != self.current_floor:

            if f_number > self.current_floor:
                self.floor_up()
            elif f_number < self.current_floor:
                self.floor_down()

        
                

h = Elevator(0, 20) 

h.go_to_floor(25)

print("\nThe elevator is moving back to the bottom floor")
h.go_to_floor(0)