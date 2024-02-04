from datetime import datetime, date
import json


def get_current_timestamp() -> str:
    return str(datetime.now())[:-4]


def create_dict_key_from(timestamp: str) -> str:
    return timestamp[11:]


def get_current_date() -> datetime.today:
    return date.today()


def create_event() -> dict:
    return {get_current_timestamp(): {'metadata': ''}}


def store_event(filepath: str, event: dict) -> None:

    with open(filepath, 'a') as f:
        json.dump(event, f, indent=None)

