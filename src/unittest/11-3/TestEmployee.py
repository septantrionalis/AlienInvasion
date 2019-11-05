import unittest 
import time
from Employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        employee = Employee("Ron", "Kinney",100000)
        self.employee = employee
        pass

    def testGiveDefaultRaise(self):
        self.employee.giveRaise()
        self.assertEqual(self.employee.salary, 105000)

    def testGiveCustomRaise(self):
        self.employee.giveRaise(100000)
        self.assertEqual(self.employee.salary, 200000)

    def test1(self):
        time.sleep(.25)

    def test2(self):
        time.sleep(.25)

    def test3(self):
        time.sleep(.25)

    def test4(self):
        time.sleep(.25)

    def test5(self):
        time.sleep(.25)

    def test6(self):
        time.sleep(.25)

unittest.main()
