class Employment:
    def __init__(self, employer_name, job_title, start_date, city_or_town, country):
        self._employer_name = employer_name
        self._job_title = job_title
        self._start_date = start_date
        self._city_or_town = city_or_town
        self._country = country

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
