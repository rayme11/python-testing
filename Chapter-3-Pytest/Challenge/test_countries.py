# test_countries.py
import pytest
from countries import Countries

class Test_Countries():
    @pytest.fixture
    def countries_Fixture(self):
        return Countries()

    def test_add_country(self,countries_Fixture):
        countries_Fixture.add_country('01', 'USA')
        assert countries_Fixture.get_countries() == {'01': 'USA'}

    def test_update_country(elf,countries_Fixture):
        countries_Fixture.add_country('01', 'USA')
        countries_Fixture.update_country('01', 'United States')
        assert countries_Fixture.get_countries() == {'01': 'United States'}

    def test_update_nonexistent_country(elf,countries_Fixture):
        countries_Fixture.update_country('05', 'New Country')
        assert countries_Fixture.get_countries() == {}

    def test_remove_country(elf,countries_Fixture):
        countries_Fixture.add_country('01', 'USA')
        countries_Fixture.remove_country('01')
        assert countries_Fixture.get_countries() == {}

    def test_remove_nonexistent_country(elf,countries_Fixture):
        countries_Fixture.remove_country('05')
        assert countries_Fixture.get_countries() == {}

