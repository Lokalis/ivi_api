import requests as r


class Base_req():

    def __init__(self, app):
        self.app = app

    _session = r.session()

    def get_method(self, url, params=None, auth=None):
        if auth is None:
            auth = self.app.auth
        result = self._session.get(url, params=params, auth=auth, headers=self.app.headers)
        return result

    def post_method(self, url, json=None, auth=None):
        if auth is None:
            auth = self.app.auth
        result = self._session.post(url, headers=self.app.headers, json=json, auth=auth)
        return result

    def delete_method(self, url, auth=None):
        if auth is None:
            auth = self.app.auth
        result = self._session.delete(url, headers=self.app.headers, auth=auth)
        return result

    def put_method(self, url, json=None, auth=None):
        if auth is None:
            auth = self.app.auth
        result = self._session.put(url, headers=self.app.headers, json=json, auth=auth)
        return result
