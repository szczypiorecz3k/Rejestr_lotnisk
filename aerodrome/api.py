from ninja import Router
from ninja.errors import HttpError

from .models.aerodrome import Aerodrome
from .schemas.out_schemas import AerodromeOutSchema
from .repositories.aerodrome_repository import AerodromeRepository
from .repositories.runway_repository import RunwayRepository
from .use_cases.add_aerodrome_use_case import AddAerodromeWithRunwaysInputDto, AddAerodromeWithRunwaysUseCase

aerodrome_router = Router()


@aerodrome_router.get('/', response=list[AerodromeOutSchema])
def get_aerodromes(request):
    return Aerodrome.objects.all()


@aerodrome_router.get('/{icao_code}', response=AerodromeOutSchema)
def get_aerodrome(request, icao_code: str):
    try:
        return Aerodrome.objects.get(icao_code=icao_code.upper())
    except Aerodrome.DoesNotExist:
        raise HttpError(404, 'Aerodrome not found') from None


@aerodrome_router.post('/')
def add_aerodrome_with_runways(request, data: AddAerodromeWithRunwaysInputDto) -> str:
    use_case = AddAerodromeWithRunwaysUseCase(
        AerodromeRepository(), RunwayRepository())
    use_case.execute(data)

    return 'Aerodrome created'
