from aerodrome.models.runway import Runway
from aerodrome.models.aerodrome import Aerodrome
from .aerodrome_repository import AerodromeRepository
from django.db.models import QuerySet


class RunwayRepository:
    @staticmethod
    def get_by_aerodrome(aerodrome_icao_code) -> QuerySet[Runway]:
        return Runway.objects.filter(aerodrome=aerodrome_icao_code)

    @staticmethod
    def get_by_aerodrome_icao_code(icao_code) -> QuerySet[Runway]:
        return Runway.objects.filter(aerodrome__icao_code=icao_code)

    @staticmethod
    def create(len: int, code: str, aerodrome: Aerodrome) -> Runway:
        """
        Create runway

        len: int - total length of a runway
        code: str - 2 to 3 char code consisting of two digits and one letter L,C or R (optional)
        aerodrome: Aerodrome - aerodrome object where the runway is located
        """

        return Runway.objects.create(len=len,
                                     code=code,
                                     aerodrome=aerodrome)
