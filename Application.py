from Service_req.Base_req import Base_req
from Service_req.Create_instance_req import Create_instance_req
from Service_req.Delete_instance_req import Delete_instance_req
from Service_req.Modify_instance_req import Modify_instance_req
from Service_req.Search_instance_req import Search_instance_req


class App():

    def __init__(self):
        self.Create_instance_req = Create_instance_req(self)
        self.Delete_instance_req = Delete_instance_req(self)
        self.Modify_instance_req = Modify_instance_req(self)
        self.Search_instance_req = Search_instance_req(self)
        self.Base_req = Base_req(self)

    auth = ('Volkov.denis.vad@yandex.ru','hgJH768Cv23')

    api_url = 'http://rest.test.ivi.ru/v2'
    collection_url = '/characters'
    instance_collection_url = '/character'
    reset_collection_url = '/reset'

    max_items_collections = 500

    headers = {
        'Content-Type': 'application/json'
    }