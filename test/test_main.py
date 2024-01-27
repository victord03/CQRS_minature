from datetime import datetime

from src import main
import pytest

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

pytest_mark_jsons = pytest.mark.parametrize(
    'py_dict,json_string',
    [
        (victor, '{"name": "Victor", "age": 32, "male": true, "height": 1.83}'),
        (george, '{"name": "George", "age": 23, "male": true, "height": 1.74}')
    ]
)

pytest_mark_beautify_json = pytest.mark.parametrize(
    'py_dict, beautified_json',
    [
        (victor, '''{
    "age": 32,
    "height": 1.83,
    "male": true,
    "name": "Victor"
}'''),
        (george, '''{
    "age": 23,
    "height": 1.74,
    "male": true,
    "name": "George"
}'''),
    ]
)


def setup_book():
    title = ""
    category = ""
    author = ""
    year = 00
    page_count = 00
    price = 0.0
    return main.Book(
        title=title, category=category, author=author, year=year, page_count=page_count, price=price
    )


def setup_customer():
    uid = 0
    address = ""
    return main.Customer(uid=uid, address=address)


def setup_event():
    timestamp = datetime.now()
    customer = setup_customer()
    action = ""
    return main.Event(
        timestamp=timestamp,
        customer=customer,
        action=action
    )


def setup_event_store():
    db = {}
    return main.EventStore(db=db)


def test_class_book():
    res = setup_book()
    assert isinstance(res, main.Book)


def test_customer():
    res = setup_customer()
    assert isinstance(res, main.Customer)


def test_class_event():
    res = setup_event()
    assert isinstance(res, main.Event)


def test_class_event_store():
    res = setup_event_store()
    assert isinstance(res, main.EventStore)


@pytest_mark_jsons
def test_convert_a_python_dict_to_a_json_string(py_dict, json_string):
    assert main.convert_a_python_dict_to_a_json_string(py_dict) == json_string


@pytest_mark_beautify_json
def test_beautify_a_python_dict_for_printing(py_dict, beautified_json):
    assert main.beautify_a_python_dict_for_printing(py_dict) == beautified_json


def test_append_to_the_json_file():
    ...
