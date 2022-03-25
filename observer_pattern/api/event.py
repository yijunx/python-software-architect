# lets write an event file to control what 
# to do for register user


from typing import Callable


subscribers: dict[str, list[Callable]] = dict()


def subscribe(event_type: str, fn: Callable):
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)
