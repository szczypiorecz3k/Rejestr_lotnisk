from ninja import NinjaAPI

from Rejestr_lotnisk.api import aerodromer_router

api = NinjaAPI()
api.add_router('/aerodrome/', aerodromer_router)
