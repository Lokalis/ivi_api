import requests as r

default_auth = ('Volkov.denis.vad@yandex.ru', 'hgJH768Cv23')

api_url_v2 = 'http://rest.test.ivi.ru/v2'
collection_url = '/characters'
instance_collection_url = '/character'
reset_collection_url = '/reset'

max_items_collections = 500

headers = {
    'Content-Type': 'application/json'
}

def get_method(url, params=None, auth=None):
    if auth is None:
        auth = default_auth
    result = r.get(url, params=params, auth=auth, headers=headers)
    return result

def post_method(url, json=None, auth=None):
    if auth is None:
        auth = default_auth
    result = r.post(url, headers=headers, json=json, auth=auth)
    return result

def delete_method(url, auth=None):
    if auth is None:
        auth = default_auth
    result = r.delete(url, headers=headers, auth=auth)
    return result

def put_method(url, json=None, auth=None):
    if auth is None:
        auth = default_auth
    result = r.put(url, headers=headers, json=json, auth=auth)
    return result
