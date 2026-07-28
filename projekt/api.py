from ninja import NinjaAPI

from aerodrome.api import aerodrome_router

api = NinjaAPI()
api.add_router('/aerodrome/', aerodrome_router)
