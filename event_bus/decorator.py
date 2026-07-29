from .base_event import BaseEvent
from functools import wraps
from .event_bus import event_bus


def event_handler(event_type: type[BaseEvent]):
    print('event handler called')

    def decorator(func: callable):
        print('register', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        event_bus.subcribe(event_type=event_type, event_handler=func)
        return wrapper
    return decorator
