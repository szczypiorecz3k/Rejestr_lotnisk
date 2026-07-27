from pydantic import BaseModel
from injector import inject
from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.repositories.runway_repository import RunwayRepository
from aerodrome.exceptions import AerodromeAddAerodromeUseCaseError, AerodromeAddRunwayUseCaseError


class AddAerodromeInputDto(BaseModel):
    icao_code: str
    name: str
    city: str


class AddAerodromeWithRunwaysInputDto(AddAerodromeInputDto):
    runways: list[CreateRunwayInputDto]


class CreateRunwayInputDto(BaseModel):
    len: int
    code: str


class AddAerodromeUseCase:
    @inject
    def __init__(self, aerodrome_repository: AerodromeRepository):
        self.aerodrome_repository = aerodrome_repository

    def execute(self, input_dto: AddAerodromeInputDto):
        try:
            self.aerodrome_repository.create(
                icao_code=input_dto.icao_code,
                name=input_dto.name,
                city=input_dto.city,
            )
        except Exception as exc:
            raise AerodromeAddAerodromeUseCaseError(
                input_dto.icao_code) from exc


class AddAerodromeWithRunwaysUseCase:
    @inject
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
