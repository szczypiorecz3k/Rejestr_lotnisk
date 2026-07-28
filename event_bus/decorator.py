from .base_event import BaseEvent
from functools import wraps
from .event_bus import event_bus


def event_handler(event_type: type[BaseEvent]):
    def decorator(func: callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        event_bus.subcribe(event_types=event_type, event_handler=func)
        return wrapper
    return decorator
