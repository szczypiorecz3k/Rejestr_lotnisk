from ninja import Schema


class AerodromeSchema(Schema):
    icao_code: str
    name: str
    city: str
