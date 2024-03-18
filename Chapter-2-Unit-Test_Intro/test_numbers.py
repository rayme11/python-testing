import unittest
import array
from simpleNumbersClass import SomeValues

class NumbersTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
     
        
    def test_numbers_are_greater_than_1(self):
        values = SomeValues()
    
        for i in values.createNumbers():
           self.assertGreater(i,0)
           if (i > 0 ):
            print("The item is greater than 0 ::", i)
       
        
           
