import hashlib
import datetime
from os import confstr
import database
import json



#TODO: check if long URL exists
def create_hash(long_url, username):
    hash = hashlib.shake_256(long_url.encode()).hexdigest(10)
    short_url = f'tiny.com/{hash}'
    if(database.getData(short_url) is not None):
        raise ValueError("Key is already present")
    data = {
        'long_url':long_url,
        'created_by': username,
        'created_datetime': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        'used_count': 1
    }
    database.putURL(short_url, data)
    return short_url

def get_long_url(short_url):
    data = database.getData(short_url)
    if(data is None):
        raise KeyError
    else:
        data = json.loads(data)
    database.updateCount(short_url)
    return data['long_url']


def get_url_usage(short_url):
    data = database.getData(short_url)
    if(data is None):
        raise KeyError
    else:
        data = json.loads(data)
    return data
