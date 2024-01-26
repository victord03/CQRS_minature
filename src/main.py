"""Victor's Books"""
from datetime import datetime


class Book:
    title: str
    category: str
    author: str
    year: int
    page_count: int

    def __init__(self, title, category, author, year, page_count):
        self.title = title
        self.category = category
        self.author = author
        self.year = year
        self.page_count = page_count


class Event:
    """Inbound query"""

    timestamp: datetime
    customer: id
    book_title: str
    price: float
    address: str

    def __init__(self, timestamp, customer, book_title, price, address):
        self.timestamp = timestamp
        self.customer = customer
        self.book_title = book_title
        self.price = price
        self.address = address


class EventStore:
    """Write DB"""

    metadata: list
    payload: str

    def __init__(self, metadata, payload):
        self.metadata = metadata
        self.payload = payload
