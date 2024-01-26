from datetime import datetime

from src import main
import pytest

pytest_mark = pytest.mark.parametrize()


def setup_event():
    timestamp = datetime.now()
    customer = 1
    book_title = ""
    price = 0.0
    address = ""
    return main.Event(
        timestamp=timestamp,
        customer=customer,
        book_title=book_title,
        price=price,
        address=address,
    )


def setup_event_store():
    metadata = []
    payload = ""
    return main.EventStore(metadata=metadata, payload=payload)


def setup_book():
    title = ""
    category = ""
    author = ""
    year = 00
    page_count = 00
    return main.Book(
        title=title, category=category, author=author, year=year, page_count=page_count
    )


def test_class_event():
    res = setup_event()
    assert isinstance(res, main.Event)


def test_class_event_store():
    res = setup_event_store()
    assert isinstance(res, main.EventStore)


def test_class_book():
    res = setup_book()
    assert isinstance(res, main.Book)
