"""Victor's Books"""
from datetime import datetime
import json
import sqlite3

'''
'''


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
    db = dict

    def __init__(self, db):
        self.db = db


def append_to_the_json_file(existing_file_path, python_dict):
    with open(existing_file_path, 'a') as json_file:
        json.dump(python_dict, json_file)


def convert_a_python_dict_to_a_json_string(python_dict):
    return json.dumps(python_dict)


def beautify_a_python_dict_for_printing(python_dict):
    return json.dumps(python_dict, indent=4, sort_keys=True)


def main():

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


if __name__ == '__main__':
    main()
