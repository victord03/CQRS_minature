"""Victor's Books"""
from datetime import datetime
import json
from enum import Enum


class Book:
    """Business data"""

    isbn: int
    title: str
    category: str
    price: float

    def __init__(self, uid, title, category, price):
        self.isbn: uid
        self.title = title
        self.category = category
        self.price = price


class Customer:
    """Personal data. To complete any transaction we assume a valid payment method present in the account
    which does not appear here."""

    customer_ID: int
    address: str

    def __init__(self, uid, address):
        self.customer_ID = uid
        self.address = address


class EventType(Enum):
    """Types of Events"""
    ADD_TO_CART = 1
    PURCHASE = 2


class Event:
    """Inbound command (requests storing of information and does not return any value)"""

    timestamp: datetime
    event_ID: int
    customer_ID: int
    customer_address: str
    action: EventType
    item: Book

    def __init__(self, customer_uid, customer_address, action, item):
        self.timestamp = datetime.now()
        self.event_ID = int(str(self.timestamp)[-3:])
        self.customer_ID = customer_uid
        self.customer_address = customer_address
        self.action = action
        self.item = item


def generate_event_log(event) -> dict:

    item = event.item
    event_meta_data = (item.action, item.timestamp, item.customer_ID)
    event_payload = (item.customer_ID, item.price, item.author, item.year, item.title)

    return dict(
        key=event.customer_ID,
        value={
            'event_meta_data': event_meta_data,
            'event_payload': event_payload
        }
    )


def append_to_the_json_file(existing_file_path, python_dict) -> None:
    with open(existing_file_path, 'a') as json_file:
        json.dump(python_dict, json_file)


def convert_a_python_dict_to_a_json_string(python_dict) -> str:
    return json.dumps(python_dict)


def beautify_a_python_dict_for_printing(python_dict) -> str:
    return json.dumps(python_dict, indent=4, sort_keys=True)


def main():

    json_file = 'people_data.txt'

    victor = {
        'name': 'Victor',
        'age': 32,
        'male': True,
        'height': 1.83
    }

    george = {
        'name': 'George',
        'age': 23,
        'male': True,
        'height': 1.74
    }

    customer = Customer(uid=8, address="Altair St. 2, Brooklyn")
    book = Book(
        uid=1,
        title='Stables & Horses',
        category='Professional',
        price=33.45
    )
    event = Event(customer.customer_ID, customer.address, action=2, item=book)
    print(event)


if __name__ == '__main__':
    main()
