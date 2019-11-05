from Car import Car

class ElectricCar(Car):
    def __init__(self, name):
        print("Creating an ElecticCar")
        super().__init__(name)

    def refill(self):
        print("Recharging")

