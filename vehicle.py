class vehicle:
    def __init__(self, make,color):
        self.make = make
        self.color = color

    def accelerate(self):
        print("Acceleration start")
    def hoot(self):
         print("Honk Honk")
class Bus(vehicle):
    def __init__(self, make, color,passengers):
        super().__init__(make,color)
       
        self.passenger = passengers
    def start_boarding(self):
        print("The bus is boarding")
class lorry(vehicle):
    def __init__(self, make, color,max_load):
        super().__init__(make, color)
        self.max_load = max_load

    def unload(self):
        print("Unlocking")


