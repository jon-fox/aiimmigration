# from thefuzz import fuzz
from thefuzz import process

class Address():
    def __init__(self, street_number_and_name, city_or_town, state, zip_code, country, physical_addresses, mailing_address):
        self._street_number_and_name = street_number_and_name
        self._city_or_town = city_or_town
        self._state = state
        self._zip_code = zip_code
        self._country = country
        self._physical_addresses = physical_addresses if physical_addresses is not None else []  # List of Address instances
        self._mailing_address = mailing_address

    @property
    def street_number_and_name(self):
        return self._street_number_and_name

    @street_number_and_name.setter
    def street_number_and_name(self, value):
        # Add validation or processing logic here if needed
        self._street_number_and_name = value

    @property
    def city_or_town(self):
        return self._city_or_town

    @city_or_town.setter
    def city_or_town(self, value):
        self._city_or_town = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def mailing_address(self):
        return self._mailing_address
    
    @property
    def physical_addresses(self):
        return self._physical_addresses

class Employment():
    def __init__(self, employer_name, job_title, start_date, city_or_town, country, employment_history):
        self._employer_name = employer_name
        self._job_title = job_title
        self._start_date = start_date
        self._city_or_town = city_or_town
        self._country = country
        self._employment_history = employment_history if employment_history is not None else []

    @property
    def employer_name(self) -> str:
        return self._employer_name

    @employer_name.setter
    def employer_name(self, value: str) -> None:
        self._employer_name = value

    @property
    def job_title(self) -> str:
        return self._job_title

    @job_title.setter
    def job_title(self, value: str) -> None:
        self._job_title = value

    @property
    def start_date(self) -> str:
        return self._start_date

    @start_date.setter
    def start_date(self, value: str) -> None:
        self._start_date = value

    @property
    def city_or_town(self) -> str:
        return self._city_or_town

    @city_or_town.setter
    def city_or_town(self, value: str) -> None:
        self._city_or_town = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        self._country = value
    
    @property
    def employment_history(self):
        return self._employment_history

class Person():
    def __init__(self, employment, address, first_name, last_name, a_number=None, ssn=None, date_of_birth=None, country_of_birth=None, mailing_address=None, physical_addresses=None, current_marital_status=None, employment_history=None, parents=None):
        self._first_name = first_name
        self._last_name = last_name
        self.employment = employment # instance of employment class
        self.address = address # instance of address class
        self._date_of_birth = date_of_birth
        self._country_of_birth = country_of_birth
        self._current_marital_status = current_marital_status
        self._ssn = ssn
        self._a_number = a_number
        self._parents = parents if parents is not None else []

    @property
    def ssn(self):
        return self._ssn
    
    @property
    def a_number(self):
        return self._a_number
    
    @property
    def parents(self):
        return self._parents

    @property
    def first_name(self):
        return self._first_name

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
    def current_marital_status(self):
        return self._current_marital_status


def get_all_properties(obj, parent_prefix=""):
    """Recursively gather all properties and their full paths."""
    properties = {}
    attributes = [attr for attr in dir(obj) if not attr.startswith("__") and not callable(getattr(obj, attr))]
    
    for attr in attributes:
        prop = getattr(obj, attr)
        prop_type = getattr(type(obj), attr, None)

        # Construct full property path with context
        full_prop_name = f"{parent_prefix}.{attr}" if parent_prefix else attr

        if isinstance(prop_type, property):
            properties[full_prop_name] = prop
        elif hasattr(prop, '__dict__') or isinstance(prop, list):
            # Recursively get properties if it's a custom class instance or list of instances
            if isinstance(prop, list):
                # Handle each item in the list if they are custom class instances
                for index, item in enumerate(prop):
                    if hasattr(item, '__dict__'):
                        nested_properties = get_all_properties(item, f"{full_prop_name}[{index}]")
                        properties.update(nested_properties)
            else:
                nested_properties = get_all_properties(prop, full_prop_name)
                for key, value in nested_properties.items():
                    simplified_key = key.split(".")[-1]
                    properties[simplified_key] = value
        # print(f"Attribute {attr}")

    return properties

def get_closest_method_name(obj, query: str) -> str:
    # Include methods and properties in the list
    # attributes = [attr for attr in dir(obj) if not attr.startswith("__")]
    # # Filter to include callables and property instances
    # filtered_attributes = []
    # for attr in attributes:
    #     if callable(getattr(obj, attr)):
    #         filtered_attributes.append(attr)
    #     else:
    #         print(f"Attribute {attr}")
    #         # Check if the attribute is a property
    #         prop = getattr(type(obj), attr, None)
    #         if isinstance(prop, property):
    #             filtered_attributes.append(attr)
    properties = get_all_properties(obj)
    property_names = list(properties.keys())
    # print(f'Properties {property_names}')

    closest_match, score = process.extractOne(query, property_names)
    if score > 90:  # This threshold can be adjusted
        # print("Getting Closest Match " + " | " + str(filtered_attributes))
        print("PRETTY CLOSE MATCH " + closest_match + " | query " + query)
        return closest_match
    else:
        return None
    
def input_with_validation(prompt, type_=None, min_=None, max_=None, range_=None):
    """Generic input function that includes validation."""
    while True:
        try:
            value = input(prompt)
            if type_ is not None:
                value = type_(value)
            if min_ is not None and value < min_:
                raise ValueError(f"Value must be at least {min_}.")
            if max_ is not None and value > max_:
                raise ValueError(f"Value must be no more than {max_}.")
            if range_ is not None and value not in range_:
                raise ValueError(f"Value must be within {range_}.")
            return value
        except ValueError as ve:
            print(ve)
            continue

def setup_person():
    print("Please enter the following details for the person:")
    first_name = input_with_validation("Enter first name: ")
    last_name = input_with_validation("Enter last name: ")
    ssn = input_with_validation("Enter SSN (optional): ", type_=str)
    a_number = input_with_validation("Enter A-Number (optional): ", type_=str)
    date_of_birth = input_with_validation("Enter date of birth (YYYY-MM-DD): ")
    country_of_birth = input_with_validation("Enter country of birth: ")
    
    # Creating an Address instance
    print("Please enter address details:")
    street = input("Street number and name: ")
    city = input("City or town: ")
    state = input("State: ")
    zip_code = input("ZIP Code: ")
    country = input("Country: ")
    address = Address(street_number_and_name=street, city_or_town=city, state=state, 
                      zip_code=zip_code, country=country, physical_addresses=None, mailing_address=None)
    
    # Creating an Employment instance
    print("Please enter employment details:")
    employer_name = input("Employer name: ")
    job_title = input("Job title: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    employment_city = input("City or town of employment: ")
    employment_country = input("Country of employment: ")
    employment = Employment(employer_name=employer_name, job_title=job_title, 
                            start_date=start_date, city_or_town=employment_city, country=employment_country, employment_history=None)
    
    # Instantiate the Person class
    person = Person(employment=employment, address=address, first_name=first_name, last_name=last_name, 
                    a_number=a_number, ssn=ssn, date_of_birth=date_of_birth, country_of_birth=country_of_birth)

    return person
