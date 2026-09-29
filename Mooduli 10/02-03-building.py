class Building:

    def __init__(self, bot_f, top_f, elevators_num):
        self.bot_f = bot_f
        self.top_f = top_f
        self.elevators = []
        for i in range(elevators_num):
            self.elevators.append(Elevator(bot_f, top_f)) 

    def run_elevator(self, number, d_floor):
        self.elevators[number - 1].go_to_floor(d_floor)

    def fire_alarm(self):
        print("Attention! Fire alarm!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bot_f)

        print("All the elevators are on the bottom floor!")

class Elevator:
    def __init__(self, bot_f, top_f):
        self.bot_f = bot_f
        self.top_f = top_f
        self.current_floor = bot_f
        

    def floor_up(self):
         self.current_floor += 1
         print(f"The elevator is on the {self.current_floor}")

    def floor_down(self):
        self.current_floor -= 1
        print(f"The elevator is on the {self.current_floor}")
    
    def go_to_floor(self, f_number):
        
        if f_number > self.top_f:
            f_number = self.top_f
        elif f_number < self.bot_f:
            f_number = self.bot_f

        print(f"\nThe elevator is moving to the floor {f_number}")

        while f_number != self.current_floor:

            if f_number > self.current_floor:
                self.floor_up()
            elif f_number < self.current_floor:
                self.floor_down()

                        
b1 = Building(0, 20, 3)
b1.run_elevator(2, 13)
b1.fire_alarm()