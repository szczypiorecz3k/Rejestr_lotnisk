from ninja import Router
from ninja.errors import HttpError

from .models.aerodrome import Aerodrome
from .models.aerodrome_stats import AerodromeStats
from .queries.aerodromes_with_runways_query import AerodromeWithRunwaysQuery
from .repositories.aerodrome_repository import AerodromeRepository
from .repositories.runway_repository import RunwayRepository
from .schemas import AerodromeOutSchema
from .use_cases.add_aerodrome_use_case import (
    AddAerodromeWithRunwaysInputDto,
    AddAerodromeWithRunwaysUseCase,
)
from .use_cases.delete_aerodrome_use_case import DeleteAerodromeUseCase

aerodrome_router = Router()


@aerodrome_router.get('/', response=list[AerodromeOutSchema])
def get_aerodromes(request):
    return Aerodrome.objects.all()


@aerodrome_router.get('/total', response=int)
def get_aerodrome_counter(request) -> int:
    return AerodromeStats.objects.first().total


@aerodrome_router.get('/{icao_code}', response=AerodromeOutSchema)
def get_aerodrome(request, icao_code: str):
    try:
        return AerodromeWithRunwaysQuery.get_aerodromes_with_runways(icao_code=icao_code.upper())
    except Aerodrome.DoesNotExist:
        raise HttpError(404, 'Aerodrome not found') from None


@aerodrome_router.post('/')
def add_aerodrome_with_runways(request, data: AddAerodromeWithRunwaysInputDto) -> str:
    use_case = AddAerodromeWithRunwaysUseCase(AerodromeRepository(), RunwayRepository())
    use_case.execute(data)
    return 'Aerodrome created'


@aerodrome_router.delete('/{icao_code}')
def delete_aerodrome(request, icao_code: str) -> str:
    use_case = DeleteAerodromeUseCase(AerodromeRepository())
    use_case.execute(icao_code=icao_code)
    return 'Aerodrome deleted'
