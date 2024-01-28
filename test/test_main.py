from datetime import datetime

from os import chdir

from src import main
import pytest

json_file = 'test_people_data.txt'

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
    isbn = 0
    title = ""
    category = ""
    price = 0.0
    return main.Book(
        uid=isbn, title=title, category=category, price=price
    )


def setup_customer():
    customer_id = 1
    address = ""
    return main.Customer(uid=customer_id, address=address)


def setup_event():
    customer = setup_customer()

    customer_id = customer.customer_id
    customer_address = customer.address
    action = main.EventType.ADD_TO_CART
    item = setup_book()
    return main.Event(
        customer_uid=customer_id,
        customer_address=customer_address,
        action=action,
        item=item
    )


def test_class_book():
    res = setup_book()
    assert isinstance(res, main.Book)


def test_customer():
    res = setup_customer()
    assert isinstance(res, main.Customer)


def test_class_event():
    res = setup_event()
    assert isinstance(res, main.Event)


@pytest_mark_jsons
def test_convert_a_python_dict_to_a_json_string(py_dict, json_string):
    assert main.convert_a_python_dict_to_a_json_string(py_dict) == json_string


@pytest_mark_beautify_json
def test_beautify_a_python_dict_for_printing(py_dict, beautified_json):
    assert main.beautify_a_python_dict_for_printing(py_dict) == beautified_json


def test_append_to_the_json_file():

    chdir('./src')
    # chdir('src')

    with open(json_file, 'w') as f:
        f.close()

    main.append_to_the_json_file(existing_file_path=json_file, python_dict=victor)

    with open(json_file, 'r') as f:
        data = f.read()

    assert data == '{"name": "Victor", "age": 32, "male": true, "height": 1.83}'
