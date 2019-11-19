import requests as r


class Base_req():

    auth=('Volkov.denis.vad@yandex.ru','hgJH768Cv23')

    api_url='http://rest.test.ivi.ru/v2'
    collection_url='/characters'
    instance_collection_url='/character'
    reset_collection_url='/reset'

    max_items_collections=500

    headers={
        'Content-Type':'application/json'
    }


    @staticmethod
    def get_method(url,params=None,auth=None):
        if auth is None:
            auth=Base_req.auth
        result=r.get(url,params=params,auth=auth)
        return result

    @staticmethod
    def post_method(url, json=None,auth=None):
        if auth is None:
            auth=Base_req.auth
        result = r.post(url, headers=Base_req.headers,json=json,auth=auth)
        return result

    @staticmethod
    def delete_method(url,auth=None):
        if auth is None:
            auth=Base_req.auth
        result = r.delete(url,headers=Base_req.headers,auth=auth)
        return result

    @staticmethod
    def put_method(url,json=None,auth=None):
        if auth is None:
            auth=Base_req.auth
        result = r.put(url, headers=Base_req.headers, json=json, auth=auth)
        return result
