from event_bus.base_event import BaseEvent


class AerodromeCreatedEvent(BaseEvent):
    """Event emitted when aerodrome is created."""
    icao_code: str

    @property
    def message(self):
        return f'Aerodrome created {self.icao_code}.'
