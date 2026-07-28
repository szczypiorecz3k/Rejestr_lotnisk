
from pydantic import BaseModel
from aerodrome.repositories.runway_repository import RunwayRepository
from aerodrome.models.aerodrome import Aerodrome
from aerodrome.exceptions import AerodromeAddRunwayUseCaseError


class AddRunwayInputDto(BaseModel):
    len: int
    code: str
    aerodrome: Aerodrome | None = None


class AddRunwayUseCase:
    def __init__(self, runway_repository: RunwayRepository):
        self.runway_repository = runway_repository

    def execute(self, input_dto: AddRunwayInputDto):
        try:
            self.runway_repository.create(
                len=input_dto.len,
                code=input_dto.code,
                aerodrome=input_dto.aerodrome,
            )
        except Exception as exc:
            raise AerodromeAddRunwayUseCaseError(input_dto.code) from exc
