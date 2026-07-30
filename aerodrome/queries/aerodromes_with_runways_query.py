from ..repositories.aerodrome_repository import AerodromeRepository
from ..repositories.runway_repository import RunwayRepository
from ..schemas import AerodromeWithRunwaysOutSchema, RunwayOutSchema
from aerodrome.models.aerodrome_stats import AerodromeStats


class AerodromeWithRunwaysQuery:
    @staticmethod
    def get_aerodromes_with_runways(icao_code: str) -> AerodromeWithRunwaysOutSchema:
        """
        Returns aerodrome with a list of runways by icao_code
        """
        aerodrome = AerodromeRepository.get_by_icao_code(icao_code=icao_code)
        runways = RunwayRepository.get_by_aerodrome(
            aerodrome_icao_code=aerodrome)

        return AerodromeWithRunwaysOutSchema(
            icao_code=aerodrome.icao_code,
            name=aerodrome.name,
            city=aerodrome.city,
            runways=[RunwayOutSchema(len=runway.len, code=runway.code)
                     for runway in runways],
        )
