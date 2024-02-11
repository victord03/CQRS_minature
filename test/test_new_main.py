from src import new_main as nm

# import pytest
import json
from datetime import datetime, date

"""
str(date.today()) returns '2024-01-28'
str(datetime.now())[:-4] returns centi seconds

"""

testing_file_path = "/Users/victorkaklamanis/My Projects/CQRS_minature/src/test_quick_save.txt"


def test_get_current_timestamp():
    assert nm.get_current_timestamp() == str(datetime.now())[:-4]


def test_get_current_date():
    assert nm.get_current_date() == date.today()


def test_create_event():
    """dict(
        key=event.event_id,
        value={
            'event_meta_data': event_meta_data,
            'event_payload': event_payload
        }
    )"""
    assert nm.create_event() == {nm.get_current_timestamp(): {"metadata": ""}}


def test_store_event():

    with open(testing_file_path, "w") as f:
        f.close()

    new_event = nm.create_event()
    new_event_as_json_string = json.dumps(new_event)

    nm.store_event(testing_file_path, new_event)

    with open(testing_file_path, "r") as f:
        content = f.read()

    assert content == new_event_as_json_string
