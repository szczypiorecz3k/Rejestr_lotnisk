from pydantic import BaseModel
from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.repositories.runway_repository import RunwayRepository
from aerodrome.exceptions import AerodromeAddAerodromeUseCaseError, AerodromeAddRunwayUseCaseError
from event_bus.event_bus import event_bus
from ..events import AerodromeCreatedEvent


class AddAerodromeInputDto(BaseModel):
    icao_code: str
    name: str
    city: str


class CreateRunwayInputDto(BaseModel):
    len: int
    code: str


class AddAerodromeWithRunwaysInputDto(AddAerodromeInputDto):
    runways: list[CreateRunwayInputDto]


class AddAerodromeUseCase:
    def __init__(self, aerodrome_repository: AerodromeRepository):
        self.aerodrome_repository = aerodrome_repository

    def execute(self, input_dto: AddAerodromeInputDto):
        try:
            aerodrome = self.aerodrome_repository.create(
                icao_code=input_dto.icao_code,
                name=input_dto.name,
                city=input_dto.city,
            )
        except Exception as exc:
            print(exc)
            raise AerodromeAddAerodromeUseCaseError(
                input_dto.icao_code) from exc
        event_bus.publish(AerodromeCreatedEvent(icao_code=aerodrome.icao_code))


class AddAerodromeWithRunwaysUseCase:
    def __init__(self, aerodrome_repository: AerodromeRepository, runway_repository: RunwayRepository):
        self.aerodrome_repository = aerodrome_repository
        self.runway_repository = runway_repository

    def execute(self, input_dto: AddAerodromeWithRunwaysInputDto):
        try:
            aerodrome = self.aerodrome_repository.create(
                icao_code=input_dto.icao_code,
                name=input_dto.name,
                city=input_dto.city,
            )
        except Exception as exc:
            raise AerodromeAddAerodromeUseCaseError(
                input_dto.icao_code) from exc

        for runway in input_dto.runways:
            try:
                self.runway_repository.create(
                    len=runway.len,
                    code=runway.code,
                    aerodrome=aerodrome,
                )
            except Exception as exc:
                raise AerodromeAddRunwayUseCaseError(runway.code) from exc
        event_bus.publish(AerodromeCreatedEvent(icao_code=aerodrome.icao_code))
