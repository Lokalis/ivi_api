from Service_req.Base_req import *


def number_items_collection(api_url):
    """Метод возвращает кол-во элементов в коллекции"""
    url = api_url+collection_url
    instances = get_method(url)
    number_items = len(instances.json()['result'])
    return number_items

def search_instance(api_url, name, auth=None):
    """Метод поиска экземляров коллекции по свойству name

        Метод составляет валидное имя из переданой строки name
        Валидное имя - если имя указано из нескольких слов - между ними нужно ставить знак +"""

    name = '+'.join(name.split())
    url = f'{api_url}{instance_collection_url}?name={name}'
    result = get_method(url, auth=auth)
    return result

def data_search_construct(test_case):
    """Метод создания строки запроса данных тест-кейса на поиск экземляра"""
    data = '?name='
    if test_case['value'] == 'miss':
        data = ''
    else:
        data += test_case['value']
    return data
