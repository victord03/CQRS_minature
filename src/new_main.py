from datetime import datetime, date
import json

def get_current_timestamp():
    return str(datetime.now())[:-4]

def get_current_date():
    return date.today()

