from collections import defaultdict
from collections.abc import Callable


from .base_event import BaseEvent


class EventBus:
    # zrobić singleton?
    def __init__(self):
        self._handlers = defaultdict(list)

    def subcribe(self, event_types: list[type[BaseEvent]], event_handler: Callable):
        if not callable(event_handler):
            raise ValueError('Handler must be callable')
        for event_type in event_types:
            self._handlers[event_type].append(event_handler)

    def publish(self, event: BaseEvent) -> None:
        for handler in self._handlers[type(event)]:
            handler(event)


event_bus = EventBus()
