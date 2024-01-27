"""Victor's Books"""
from datetime import datetime
import json

'''
a) Open a .json file

        with open('file_path.json', 'r') as f:
            data = json.load(f)

b) Convert a python dict to a .json string

        py_dict = {
            'key': 'value',
        }
        
        json_string = json.dumps(json_str)

c) Write to a .json file

        py_dict = {
            'key': 'value',
        }
        
        with open('file_path.txt', 'w') as json_file:
            json.dump(py_dict, json_file)
    
d) Pretty print

        print(json.dumps(py_dict, indent=4, sort_keys=True))
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

    def __init__(self, metadata, payload):
        self.metadata = metadata
        self.payload = payload


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

    # json_string = json.dumps(py_dict)

    with open('people_data.txt', 'a') as json_file:
        json.dump(george, json_file)

    # print(json.dumps(py_dict, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
