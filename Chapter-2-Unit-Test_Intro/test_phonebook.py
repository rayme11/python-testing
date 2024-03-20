import unittest
from phonebook import Phonebook
import logging

class PhonebookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook()
   
    def tearDown(self) -> None:
        return super().tearDown()
        pass

    def test_look_by_name(self):
       
        self.phonebook.add("Ray", "12345")
        number = self.phonebook.lookup("Ray")
        self.assertEqual(number, "12345")

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missingnumber")

    def test_empty_phone_is_consistent(self):
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)