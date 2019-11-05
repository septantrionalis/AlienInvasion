class Car:
    def __init__(self, name):
        print("Creating a Car")
        self.name = name
        self.odometer = 0

    def refill(self):
        print("Refueling")

    def getOdometer(self):
        return self.odometer

    def getName(self):
        return self.name

    def move(self, mileage):
        '''moves the car'''
        if (mileage >= 0):
            print(self.getName() + " moved " + str(mileage) + " miles")
            self.odometer += mileage
        else:
           print("Cant rollback the odometer")
            
