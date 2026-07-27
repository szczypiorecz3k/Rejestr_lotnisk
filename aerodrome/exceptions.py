from projekt.exceptions import BaseError


class AerodromeError(BaseError):
    pass


class AerodromeAddAerodromeUseCaseError(AerodromeError):
    def __init__(self, icao_code: str):
        self.details = f'Failed to create aerodrome {icao_code}.'
        super().__init__(self.details)


class AerodromeAddRunwayUseCaseError(AerodromeError):
    def __init__(self, code):
        self.details = f'Failed to create runway {code}.'
        super().__init__(self.details)
