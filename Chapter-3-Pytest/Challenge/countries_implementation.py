# main_script.py

from countries import Countries

print("Beginning Unit Testing")

countries_instance = Countries()


def add_countries():
    countries_instance.add_country('01', 'USA')
    countries_instance.add_country('02', 'MX')
    countries_instance.add_country('03', 'CHILE')
    countries_instance.add_country('04', 'ARGENTINA')


def get_countries():
    countries = countries_instance.get_countries()
    for code, name in countries.items():
        print(f"Country Code: {code}, Country Name: {name}")


def update_country():
    countries_instance.update_country('01', 'United States')  # Update USA to United States
    countries_instance.update_country('05', 'New Country')   # Trying to update a non-existent country


def remove_country():
    countries_instance.remove_country('02')  # Remove Mexico
    countries_instance.remove_country('05')  # Trying to remove a non-existent country


def main():
    print("Here we go..adding some countries first..")
    add_countries()
    print("Getting countries..")
    get_countries()
    print("Updating country..")
    update_country()
    print("Getting countries after update..")
    get_countries()
    print("Removing country..")
    remove_country()
    print("Getting countries after removal..")
    get_countries()


if __name__ == "__main__":
    main()
