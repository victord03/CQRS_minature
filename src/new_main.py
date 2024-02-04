from datetime import datetime, date
import json


def get_current_timestamp():
    return str(datetime.now())[:-4]


def create_dict_key_from(timestamp: str):
    return timestamp[11:]


def get_current_date():
    return date.today()


def create_event():
    return {get_current_timestamp(): {'metadata': ''}}


# print(get_current_timestamp())
# print(create_dict_key_from(get_current_timestamp()))
