from ninja import Schema


class AerodromeSchema(Schema):
    icao_code: str
    name: str
    city: str


class RunwaySchema(Schema):
    len: int
    code: str


class AerodromeWithRunwaysSchema(AerodromeSchema):
    runways: list[RunwaySchema]
