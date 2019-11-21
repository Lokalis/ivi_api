from Data_tests import data_create_instance
from Service_req.Create_instance_req import Create_instance_req
import pytest


@pytest.mark.skip_api_url_fail
class Test_create_instance():

    @pytest.mark.parametrize('role,auth,code_except', [('basic', None, 200), ('invalid full auth', ('awdawdawd', 'awd'), 401),('invalid email',('den','hgJH768Cv23'),401)])
    def test_access_resource_method(self, api_url, arrange_create_character, role, auth, code_except):
        f"""Выполнение запросов на создание экземляра коллекции с аутентификацией {role}"""
        result = arrange_create_character(api_url, auth=auth)
        assert result.status_code == code_except, f'\nНекорректный код ответа на запрос создания экземпляра с ' \
            f'aутентификацией {role} \nAuth: {auth} \nЗапрос: POST \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Create_instance_req.get_test_case(data_create_instance.data_negative_create))
    def test_negative_create_instance(self, api_url, arrange_create_character, property, test_case, client):
        """Запросы на создание экземпляра коллекции с некорректными свойствами"""
        data = client.Create_instance_req.data_create_construct(test_case, property)
        result = arrange_create_character(api_url, data=data)
        assert result.status_code == 400 and result.json()['error'] == test_case['error'], f'\nНекорректная ошибка в теле ответа \nЗапрос : POST  ' \
            f' \ndata: {data} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Create_instance_req.get_test_case(data_create_instance.data_positive_create))
    def test_positive_create_instance(self, api_url, arrange_create_character, property, test_case, client):
        """Запросы на создание экземпляра коллекции с корректными свойствами"""
        data = client.Create_instance_req.data_create_construct(test_case, property)
        result = arrange_create_character(api_url, data=data)
        assert result.status_code == 200, f'\nЭкземпляр коллекции не создался \nЗапрос : POST ' \
            f' \ndata: {data} \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Create_instance_req.get_test_case(data_create_instance.data_duplicate_create))
    def test_duplicate_create_instance(self, api_url, arrange_create_character, property, test_case, client):
        """Запросы на создание экземпляра коллекции с дублирующими свойствами"""
        data_create = client.Create_instance_req.data_create_construct(test_case['case_create'], property)
        data_duplicate = client.Create_instance_req.data_create_construct(test_case['case_duplicate'], property)
        create_instance = arrange_create_character(api_url, data=data_create)
        duplicate_instance = arrange_create_character(api_url, data=data_duplicate)
        assert create_instance.status_code == 200, f'\nЭкземляр-образец не создан \nЗапрос : POST ' \
            f' \ndata: {data_create} \nResponse: {create_instance} \nResponse body: {create_instance.text}'
        assert duplicate_instance.status_code == 400 and duplicate_instance.json()['error'] == f"{test_case['case_create']['value']} is already exists",f'' \
            f'\nВозникла ошибка при создании дублирующего экземпляра \nЗапрос : POST ' \
            f' \ndata: {data_duplicate} \nExcept error: {test_case["error"]} \nResponse: {duplicate_instance} \nResponse body: {duplicate_instance.text}'

    def test_creation_limit_instance(self, api_url, client):
        """Серия запросов на создание экземпляров для тестирования ситуации переполнености базы"""
        items_now = client.Search_instance_req.number_items_collection(api_url)
        for instance in range(client.max_items_collections-items_now):
            client.Create_instance_req.create_character(api_url)
        result = client.Create_instance_req.create_character(api_url)
        assert result.status_code == 400 and result.json()['error'] == "Collection can't contain more than 500 items", f'\nБаза данных вмещает больше чем 500 персонажей'
