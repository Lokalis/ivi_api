from Service_req.Create_instance_req import Create_instance_req
from Data_tests import data_search_instance
import pytest


@pytest.mark.skip_api_url_fail
class Test_delete_instance():

    @pytest.mark.parametrize('role,auth,code_except', [('basic', None, 400), ('invalid auth', ('awdawdawd', 'awd'), 401),('invalid email',('den','hgJH768Cv23'),401)])
    def test_access_resource_method(self, api_url, code_except, role, auth, client):
        f"""Выполнение запросов на поиск экземляра коллекции с аутентификацией {role}"""
        search_name = 'random_name'
        result = client.Delete_instance_req.delete_instance(api_url, search_name,auth=auth)
        assert result.status_code == code_except, f'\nНекорректный код ответа на запрос создания экземпляра с ' \
            f'aутентификацией {role} \nAuth: {auth} \nЗапрос: DELETE \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Create_instance_req.get_test_case(data_search_instance.date_negative_search_instance))
    def test_negative_search_instance(self, api_url, arrange_create_character, property, test_case, client):
        """Запросы на создание экземпляра коллекции с некорректными свойствами"""
        if 'add_instance' in test_case:
            data_create = client.Create_instance_req.data_create_construct(test_case['add_instance'], property=property)
            arrange_create_character(api_url, data=data_create)
        data_delete = client.Search_instance_req.data_search_construct(test_case)
        result = client.Base_req.delete_method(api_url + client.instance_collection_url+data_delete)
        assert result.status_code == 400 and result.json()['error'] == test_case['error'], f'\nНекорректная ошибка в теле ответа \nЗапрос : DELETE ' \
            f' \ndata: {data_delete} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Create_instance_req.get_test_case(data_search_instance.data_positive_search_instance))
    def test_positive_search_instance(self, property, test_case, api_url, arrange_create_character, client):
        """Запросы на создание экземпляра коллекции с корректными свойствами"""
        data_create = client.Create_instance_req.data_create_construct(test_case['add_instance'], property=property)
        create_instance = arrange_create_character(api_url, data=data_create)
        data_delete = client.Search_instance_req.data_search_construct(test_case)
        result = client.Base_req.delete_method(api_url + client.instance_collection_url+data_delete)
        assert create_instance.status_code == 200,f'\nЭкземпляр коллекции для удаления не создан \nЗапрос : POST ' \
            f' \ndata: {data_create} \nResponse: {result} \nResponse body: {result.text}'
        assert result.status_code == 200 and result.json()['result']==f'Hero {create_instance.json()["result"]["name"]} is deleted', f'\nЭкземпляр не удален \nЗапрос : DELETE ' \
            f' \nparams: {data_delete} \nCreate inst data: {create_instance.json()} \nResponse: {result} \nResponse body: {result.text}'
