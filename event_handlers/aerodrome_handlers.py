from aerodrome.events import AerodromeCreatedEvent, AerodromeDeletedEvent
from aerodrome.models.aerodrome_stats import AerodromeStats
from aerodrome.models.aerodrome import Aerodrome
from aerodrome.events import AerodromeCreatedEvent, AerodromeDeletedEvent
from event_bus.decorator import event_handler


@event_handler(AerodromeCreatedEvent)
def aerodrome_created_handler(event: AerodromeCreatedEvent) -> None:
    print(event.message)


@event_handler(AerodromeCreatedEvent)
def aerodrome_created_count_handler(event: AerodromeCreatedEvent) -> None:
    counter, _ = AerodromeStats.objects.get_or_create(
        id=1,
        defaults={
            'total': 0,
            'id': 1},
    )
    counter.total = Aerodrome.objects.count()
    counter.save()
    print('Aerodrome counted.')


@event_handler(AerodromeDeletedEvent)
def aerodrome_deleted_handler(event: AerodromeDeletedEvent) -> None:
    counter = AerodromeStats.objects.first()
    counter.total = Aerodrome.objects.count()
    counter.save()
    print('Aerodrome deleted.')
