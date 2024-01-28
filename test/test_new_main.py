from src import new_main as nm
import pytest
from datetime import datetime, date

'''
str(date.today()) returns '2024-01-28'
str(datetime.now())[:-4] returns centi seconds

'''

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
    assert nm.create_event() == {'', }