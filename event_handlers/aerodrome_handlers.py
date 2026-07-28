from ..aerodrome.events import AerodromeCreatedEvent
from ..aerodrome.models.aerodrome_counter import AerodromeCounter
from ..aerodrome.models.aerodrome import Aerodrome
from ..aerodrome.events import AerodromeCreatedEvent
from ..event_bus.decorator import event_handler


@event_handler(AerodromeCreatedEvent)
def aerodrome_created_handler(event: AerodromeCreatedEvent) -> None:
    print(event.message)


@event_handler(AerodromeCreatedEvent)
def aerodrome_created_count_handler(event: AerodromeCreatedEvent) -> None:
    counter, _ = AerodromeCounter.objects.get_or_create(
        id=1,
        defaults={
            'total': Aerodrome.objects.count(),
            'id': 1},
    )
    counter.total += 1
    counter.save()
