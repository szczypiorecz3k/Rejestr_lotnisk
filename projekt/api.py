from ninja import NinjaAPI

from aerodrome.api import aerodromer_router

api = NinjaAPI()
api.add_router('/aerodrome/', aerodromer_router)
