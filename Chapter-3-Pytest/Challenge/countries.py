# countries/countries.py

class Countries:
    def __init__(self):
        self.country_dict = {}

    def add_country(self, code, name):
        self.country_dict[code] = name

    def get_countries(self):
        return self.country_dict

    def update_country(self, code, new_name):
        if code in self.country_dict:
            self.country_dict[code] = new_name
        else:
            print(f"Country with code {code} does not exist.")

    def remove_country(self, code):
        if code in self.country_dict:
            del self.country_dict[code]
        else:
            print(f"Country with code {code} does not exist.")
