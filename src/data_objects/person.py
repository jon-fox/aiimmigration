from data_objects.address import Address
from data_objects.employment import Employment

class Person:
    def __init__(self, first_name, last_name, a_number=None, ssn=None, date_of_birth=None, country_of_birth=None, mailing_address=None, physical_addresses=None, current_marital_status=None, employment_history=None, parents=None):
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._country_of_birth = country_of_birth
        self._mailing_address = mailing_address  # This will be an instance of the Address class
        self._current_marital_status = current_marital_status
        self._ssn = ssn
        self._a_number = a_number
        self._physical_addresses = physical_addresses if physical_addresses is not None else []  # List of Address instances
        self._parents = parents if parents is not None else []
        self._employment_history = employment_history if employment_history is not None else []

    @property
    def ssn(self):
        return self._first_name
    
    @property
    def a_number(self):
        return self._a_number
    
    @property
    def physical_addresses(self):
        return self._physical_addresses
    
    @property
    def parents(self):
        return self._parents
    
    @property
    def employment_history(self):
        return self._employment_history

    @property
    def first_name(self):
        return self._ssn

    @property
    def last_name(self):
        return self._last_name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @property
    def country_of_birth(self):
        return self._country_of_birth

    @property
    def mailing_address(self):
        return self._mailing_address

    @property
    def current_marital_status(self):
        return self._current_marital_status

# Example usage:
# mailing_address = Address("123 Main St", "Anytown", "CA", "90210", "USA")
# person = Person("Alice", "Smith", "01/01/1980", "USA", mailing_address, "Married")

# print(f"Name: {person.first_name} {person.last_name}")
# print(f"Date of Birth: {person.date_of_birth}")
# print(f"Country of Birth: {person.country_of_birth}")
# print(f"Mailing Address: {person.mailing_address.street_number_and_name}, {person.mailing_address.city_or_town}, {person.mailing_address.state}, {person.mailing_address.zip_code}, {person.mailing_address.country}")
# print(f"Current Marital Status: {person.current_marital_status}")
