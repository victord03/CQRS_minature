"""Victor's Books"""
from datetime import datetime


class Book:
    """Business data"""

    title: str
    category: str
    author: str
    year: int
    page_count: int
    price: float

    def __init__(self, title, category, author, year, page_count, price):
        self.title = title
        self.category = category
        self.author = author
        self.year = year
        self.page_count = page_count
        self.price = price


class Customer:
    """Personal data"""

    uid: int
    address: str

    def __init__(self, uid, address):
        self.uid = uid
        self.address = address


class Event:
    """Inbound query"""

    timestamp: datetime
    customer: Customer
    action: str

    def __init__(self, timestamp, customer, action):
        self.timestamp = timestamp
        self.customer = customer.uid
        self.address = customer.address
        self.action = action


class EventStore:
    """Write DB"""

    metadata: list
    payload: str

    def __init__(self, metadata, payload):
        self.metadata = metadata
        self.payload = payload
