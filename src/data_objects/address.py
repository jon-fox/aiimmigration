class Address:
    def __init__(self, street_number_and_name, city_or_town, state, zip_code, country):
        self._street_number_and_name = street_number_and_name
        self._city_or_town = city_or_town
        self._state = state
        self._zip_code = zip_code
        self._country = country

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

# Example usage remains the same as before
