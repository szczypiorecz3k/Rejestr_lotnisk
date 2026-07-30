from pydantic import BaseModel

from aerodrome.repositories.aerodrome_repository import AerodromeRepository
from aerodrome.repositories.runway_repository import RunwayRepository


class AddRunwayInputDto(BaseModel):
    len: int
    code: str
    aerodrome_icao_code: str | None = None


class AddRunwayUseCase:
    def __init__(self, runway_repository: RunwayRepository):
        self.runway_repository = runway_repository

    def execute(self, input_dto: AddRunwayInputDto):
        try:
            print('START')
            aerodrome = AerodromeRepository.get_by_icao_code(input_dto.aerodrome_icao_code)
            print(f'Aerodroeme {aerodrome.icao_code} found')

            self.runway_repository.create(
                len=input_dto.len,
                code=input_dto.code,
                aerodrome=aerodrome,
            )
            print('Runway created.')
        except Exception as exc:
            raise (exc)
            # raise AerodromeAddRunwayUseCaseError(input_dto.code) from exc
