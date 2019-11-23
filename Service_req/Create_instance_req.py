import random
from Service_req.Base_req import *



def random_characters_data():
    """Метод создания рандомных даных для экземпляра коллекции"""
    data = {
            'name': "".join(random.choice('testdefault') for _ in range(random.randint(10, 20)))
        }
    return data

def create_character(api_url, data='random', auth=None):
    """Метод создания экземпляра коллекции"""
    url = api_url + instance_collection_url
    if data is 'random':
            data = random_characters_data()
    result = post_method(url, json=data, auth=auth)
    return result


def data_create_construct(test_case, attribute, data=None):
    """Метод формирует тело запроса исходя из данных тест-кейса"""
    if data is None:
        data = random_characters_data()
    if attribute == 'data':
        return test_case['value']
    if test_case['value'] == 'miss':
        del data[attribute]
    else:
        data[attribute] = test_case['value']
    if 'add' in test_case:
        for atr in test_case['add']:
            property_atr = atr['attribute']
            data[property_atr] = atr['value']
    return data

def get_test_case(data_test):
    """Метод предоставляет данные для тестирования, сформированные из тест-кейсов"""
    data=[]
    for name_attribute in data_test:
        for data_test_case in data_test[name_attribute]:
          data.append(tuple([name_attribute, data_test_case]))
    return data

def reset_collection(api_url):
    """Метод сбрасывает колекцию в первоначальное состояние"""
    url = api_url+reset_collection_url
    result = post_method(url)
    return result
