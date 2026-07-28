from ..event_bus.base_event import BaseEvent


class AerodromeCreatedEvent(BaseEvent):
    """Event emitted when aerodrome is created."""

    def __init__(self, icao_code):
        self.icao_code = icao_code
        self.message = f'Aerodrome created {self.icao_code}.'
