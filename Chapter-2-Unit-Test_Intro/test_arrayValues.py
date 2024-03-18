import unittest
from simpleArrayClass import CarsCost
import array

class CarCostTest(unittest.TestCase):

    def test_numbers_are_positive(self):
        carcosts = array.array('f', CarsCost.getValues())
        print(len(carcosts))
        for i in range(0 , len(carcosts)):
                if (carcosts[i]) > 0:
                        print(carcosts[i])
                        pass
        