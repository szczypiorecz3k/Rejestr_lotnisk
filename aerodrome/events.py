from event_bus.base_event import BaseEvent


class AerodromeModifiedEvent(BaseEvent):
    """Event emitted when aerodrome is modified."""
    icao_code: str

    @property
    def message(self):
        return f'Aerodrome {self.icao_code} modified.'


class AerodromeCreatedEvent(AerodromeModifiedEvent):
    """Event emitted when aerodrome is created."""
    @property
    def message(self):
        return f'Aerodrome {self.icao_code} created.'


class AerodromeDeletedEvent(AerodromeModifiedEvent):
    """Event emitted when aerodrome is deleted."""
    @property
    def message(self):
        return f'Aerodrome {self.icao_code} deleted.'
