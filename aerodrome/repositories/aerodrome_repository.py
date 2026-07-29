from aerodrome.models.aerodrome import Aerodrome
from ..exceptions import AerodromeNotExistError


class AerodromeRepository:
    '''
    Repository for Aerodrome operations.
    '''
    @staticmethod
    def get_by_icao_code(icao_code):
        try:
            return Aerodrome.objects.get(icao_code=icao_code.upper())
        except Aerodrome.DoesNotExist:
            raise AerodromeNotExistError(icao_code=icao_code)

    @staticmethod
    def get_by_city(city):
        return Aerodrome.objects.filter(city=city)

    @staticmethod
    def create(icao_code, name, city):
        """
        Create a new Aerodrome

        icao_code: str - 4 letter aerodrome code, must be unique
        name: str - full aerodrome name
        city: str - location of the aerodrome or nearest big city
        """

        return Aerodrome.objects.create(icao_code=icao_code,
                                        name=name,
                                        city=city,
                                        )

    @staticmethod
    def delete(icao_code):
        AerodromeRepository.get_by_icao_code(icao_code=icao_code).delete()
