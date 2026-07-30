from event_bus.event_bus import event_bus

from ..events import AerodromeDeletedEvent
from ..repositories.aerodrome_repository import AerodromeRepository


class DeleteAerodromeUseCase:
    def __init__(self, aerodrome_repository: AerodromeRepository):
        self.aerodrome_repository = aerodrome_repository

    def execute(self, icao_code: str):
        self.aerodrome_repository.delete(icao_code)
        event_bus.publish(AerodromeDeletedEvent(icao_code=icao_code))
