import json
import redis

r = redis.Redis(host='redis', port=6379, db=1)


def putURL(short_url, data):
    r.set(short_url, json.dumps(data))

def updateCount(short_url):
    data = r.get(short_url)
    if data is not None:
        data = json.loads(data)
        data['used_count'] = data['used_count']+1
        r.set(short_url, json.dumps(data))


def getData(short_url):
    return r.get(short_url)