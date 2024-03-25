import pytest
from phonebook import Phonebook

class TestPhoneBookOperations:
    @pytest.fixture
    def phoneBook_Fixture(self):
        return Phonebook()
    
    def test_phone_Number_Is_Valid(self, phoneBook_Fixture):
        validNumber = phoneBook_Fixture.validate_phone_number('813-508-5819')
        assert validNumber is True

    def test_phone_Number_Is_InValid(self, phoneBook_Fixture):
        validNumber = phoneBook_Fixture.validate_phone_number('813-508-5819f')
        assert validNumber is False

    def test_phone_lenght_is_correct(self, phoneBook_Fixture):
        isValidNumber = phoneBook_Fixture.validate_phone_number_lenght('813508501999999')
        assert isValidNumber is False
    
    def test_phone_Number_Is_Valid_WithChars(self, phoneBook_Fixture):
        validNumber = phoneBook_Fixture.validate_phone_number('abc-def-5819')
        assert validNumber is False

    
    def test_phone_Number_Is_Valid_WithSpaces(self, phoneBook_Fixture):
        validNumber = phoneBook_Fixture.validate_phone_number('813-508- 819')
        assert validNumber is False

    def test_adding_phone_number(self, phoneBook_Fixture):
        validNumber = phoneBook_Fixture.add_phone_number("Ray", 813-508-5819)
        getNumber = phoneBook_Fixture.get_phone_number("Ray", 813-508-5819)
        assert getNumber is True
        
        
        
