from array_base import integer_numbers
import unittest


class someSillyTest(unittest.TestCase):
    
   

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        global mysillyNumbers
        mysillyNumbers = integer_numbers.get_numbers()


    def test_all_numbers_are_greater_than_zero(self):
        for number in range(1, len(mysillyNumbers)):
            self.assertGreater(number, 0)