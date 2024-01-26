"""Victor's Books"""
from datetime import datetime


class Event:
    """Inbound query"""
    timestamp: datetime
    customer: id
    book_title: str
    price: float
    address: str


class EventStore:
    """Write DB"""
    ...
