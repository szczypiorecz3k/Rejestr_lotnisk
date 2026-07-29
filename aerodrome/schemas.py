from ninja import Schema


class AerodromeOutSchema(Schema):
    icao_code: str
    name: str
    city: str


class RunwayOutSchema(Schema):
    len: int
    code: str


class AerodromeWithRunwaysOutSchema(AerodromeOutSchema):
    runways: list[RunwayOutSchema]
