import unittest
from phonebook import Phonebook
import logging

class PhonebookTest(unittest.TestCase):
   

    def test_look_by_name(self):
       
        phonebook = Phonebook()
        phonebook.add("Ray", "12345")

        number = phonebook.lookup("Ray")
       
        

        self.assertEqual(number, "12345")

    def test_missing_name(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missingnumber")