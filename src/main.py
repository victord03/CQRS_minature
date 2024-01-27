"""Victor's Books"""
from datetime import datetime
import json
import sqlite3
from enum import Enum

'''

I) Event storage formatting
The structure stored in the 'quick save' db will be the following:
    dict(key=id, value=tuple(event metadata, event payload))
    
i.e.
    {id: int, value: (event metadata, event payload)}
    
II) Event metadata

The event metadata will contain the following data:

        1. EventType
        2. Timestamp
        3. Customer UID

III) Event payload

The even payload will contain the following data:

        1. Book UID
        2. Book price
        3. Book author
        4. Book year
        5. Book title

'''


class Book:
    """Business data"""

    uid: int
    title: str
    category: str
    author: str
    year: int
    page_count: int
    price: float

    def __init__(self, uid, title, category, author, year, page_count, price):
        self.uid: uid
        self.title = title
        self.category = category
        self.author = author
        self.year = year
        self.page_count = page_count
        self.price = price


class Customer:
    """Personal data. To complete any transaction we assume a valid payment method present in the account
    which does not appear here."""

    uid: int
    address: str

    def __init__(self, uid, address):
        self.uid = uid
        self.address = address


class EventType(Enum):
    """Types of Events"""
    # Should auto() be used instead of hard coded values ?
    ADD_TO_CART = 1
    CLICK_ON_CART = 2
    GO_TO_CHECKOUT = 3
    PURCHASE = 4


class Event:
    """Inbound command (requests storing of information and does not return any value)"""

    timestamp: datetime
    uid: int
    customer_uid: int  # todo: requires Customer.uid
    customer_address: str  # todo: requires Customer.address
    action: EventType
    item: Book

    def __init__(self, customer_uid, customer_address, action, item):
        self.timestamp = datetime.now()
        self.uid = int(str(self.timestamp)[-3:])
        self.customer_uid = customer_uid
        self.customer_address = customer_address
        self.action = action
        self.item = item


"""class EventStore:
    '''Write DB'''

    metadata: list
    payload: str
    db = dict

    def __init__(self, db):
        self.db = db"""


def generate_event_log(event) -> dict:

    item = event.item
    event_meta_data = (item.action, item.timestamp, item.customer_uid)
    event_payload = (item.uid, item.price, item.author, item.year, item.title)

    return dict(
        key=event.uid,
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

    print(EventType(2))


if __name__ == '__main__':
    main()
