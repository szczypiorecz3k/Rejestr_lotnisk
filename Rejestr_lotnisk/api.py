from ninja import Router
from .models import Aerodrome
from .schemas import AerodromeSchema

aerodromer_router = Router()


@aerodromer_router.get('/', response=list[AerodromeSchema])
def get_aerodromes(request):
    return Aerodrome.objects.all()


@aerodromer_router.get('/{icao_code}', response=AerodromeSchema)
def get_aerodrome(request, icao_code: str):
    return Aerodrome.objects.get(icao_code=icao_code)
