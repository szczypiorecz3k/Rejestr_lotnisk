from collections import defaultdict
from collections.abc import Callable


from .base_event import BaseEvent


class EventBus:
    # zrobić singleton?
    def __init__(self):
        self._handlers = defaultdict(list)

    def subcribe(self, event_type: type[BaseEvent], event_handler: Callable):
        if not callable(event_handler):
            raise ValueError('Handler must be callable')
        self._handlers[event_type].append(event_handler)

    def publish(self, event: BaseEvent) -> None:
        for handler in self._handlers[type(event)]:
            print('Executing', handler.__name__)
            handler(event)


event_bus = EventBus()
print('EVENT BUS', id(event_bus))
