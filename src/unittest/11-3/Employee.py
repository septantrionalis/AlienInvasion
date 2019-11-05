class Employee():

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def giveRaise(self, value = 5000):
        self.salary += value


