import array
import re

class Phonebook:
    def __init__(self):
       global phonenumbers
       phonenumbers = {}

    
    def validate_phone_number(self,number):
        phone_number_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')

        # Test the regex pattern
        # phone_number = '123-456-7890'
        if phone_number_pattern.match(number):
           return True
        else:
            return False
        

    def validate_phone_number_lenght(self,number):
        
        if len(number) == 11:
            return True
        else:
            return False

    def add_phone_number(self,name, number):

        if number in phonenumbers:
            return False
        else:
            phonenumbers[name] = number
            print('item added')
            return True
        
    def get_phone_number(self,name, number):
        numbers = phonenumbers.values()
        if number in numbers:
            return True
        else:
           return False


            

    
   
        
