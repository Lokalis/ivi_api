from Service_req.Base_req import *
from Service_req.Create_instance_req import *


def modify_instance(api_url, data, auth=None):
    """Метод изменения экземпляра на основании переданных данных data"""
    url = api_url+instance_collection_url
    result = put_method(url,json=data,auth=auth)
    return result

def modify_data_construct(attribute, test_case, name):
    """Метод подготовки данных из тест-кейса"""
    data_default = {
            'name': name
        }
    data_modify = data_create_construct(attribute=attribute, test_case=test_case, data=data_default)
    return data_modify
