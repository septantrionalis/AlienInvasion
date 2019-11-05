from Car import Car
from ElectricCar import ElectricCar

class Drive:
    def __init__(self):
        print("Creating a Drive object")


electricCar = ElectricCar("SoyMobile")
car = Car("El Diablo")

electricCar.refill()
car.refill()

print(electricCar.getName() + " has " + str(electricCar.getOdometer()) + " miles.")
print(car.getName() + " has " + str(car.getOdometer()) + " miles.")

car.move(1000)

print(car.getName() + " has " + str(car.getOdometer()) + " miles.")

car.move(1001)

print(car.getName() + " has " + str(car.getOdometer()) + " miles.")

electricCar.move(-1000)
