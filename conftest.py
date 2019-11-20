import requests as r
import pytest
from Service_req.Base_req import Base_req
from Service_req.Create_instance_req import Create_instance_req
from Service_req.Search_instance_req import Search_instance_req

@pytest.fixture(scope='class')
def api_url():
    """Фикстура для получения url хоста"""
    url=Base_req.api_url
    try:
        assert r.head(url,auth=Base_req.auth).status_code==200
        return url
    except:
        return False,f'Корневой ресурс недоступен url: {url}'


@pytest.fixture(scope='class',autouse=True)
def skip_by_smoke(request, api_url):
    """Фикстура добавляет новую метку в pytest, для пропуска тестов при недоступности корневого ресурса"""
    if request.node.get_closest_marker('skip_api_url_fail'):
        if api_url[0]==False:
            pytest.skip(api_url[1])


@pytest.fixture(scope='class')
def arrange_create_character(api_url):
    """Фикстура создания элементов коллекции

    Перед каждым запуском тестов на создание экземпляра - база обнуляется к первоначальному виду
    После создания элемента - счетчик элементов items_create увеличивается на один
    Если счетчик items_create  сравняется c items_collection -  произойдет reset коллекции"""

    Create_instance_req.reset_collection(api_url)
    items_collection= Base_req.max_items_collections - Search_instance_req.number_items_collection(api_url)
    items_create=[]
    def create_character(api_url,data='random',auth=None):
        result=Create_instance_req.create_codes(api_url, data=data, auth=auth)
        if result.status_code==200:
            name=result.json()['result']['name']
            items_create.append(name)
        try:
            if len(items_create)==items_collection:
                Create_instance_req.reset_collection(api_url)
                items_create.clear()
        finally:
            return result
    yield create_character
    assert Create_instance_req.reset_collection(api_url).status_code==200