from Service_req.Create_instance_req import *
from Data_tests.data_search_instance import *
from Service_req.Search_instance_req import *
from Service_req.Delete_instance_req import *
import pytest


@pytest.mark.skip_api_url_fail
class Test_delete_instance():

    @pytest.fixture(params=get_test_case(data_positive_search_instance))
    def data_positive_test(self,request):
        test = dict()
        attribute, test_case = request.param
        test['data_delete'] = data_search_construct(test_case)
        test['data_create'] = data_create_construct(test_case['add_instance'], attribute)
        return test

    @pytest.fixture(params=get_test_case(data_negative_search_instance))
    def data_negative_test(self, request):
        test=dict()
        attribute,test_case = request.param
        test['data_delete'] = data_search_construct(test_case)
        if 'add_instance' in test_case:
            test['data_create']=data_create_construct(test_case['add_instance'], attribute)
        return test,test_case['error']

    @pytest.mark.parametrize('role,auth,code_except', [('basic', None, 400), ('invalid auth', ('awdawdawd', 'awd'), 401),('invalid email',('den','hgJH768Cv23'),401)])
    def test_access_resource_method(self, api_url, code_except, role, auth):
        f"""Выполнение запросов на удаление экземляра коллекции с аутентификацией {role}"""
        search_name = 'random_name'
        result = delete_instance(api_url, search_name,auth=auth)
        assert result.status_code == code_except, f'\nНекорректный код ответа на запрос создания экземпляра с ' \
            f'aутентификацией {role} \nAuth: {auth} \nЗапрос: DELETE \nResponse: {result} \nResponse body: {result.text}'

    def test_negative_delete_instance(self, api_url, arrange_create_character, data_negative_test):
        """Запросы на удаление экземпляра коллекции с некорректными свойствами"""
        data,error=data_negative_test
        if 'data_create' in data:
            arrange_create_character(api_url, data=data['data_create'])
        result = delete_method(api_url + instance_collection_url+data['data_delete'])
        assert result.status_code == 400,f'\nНекорректный код ответа \nЗапрос : DELETE ' \
            f' \ndata: {data["data_delete"]} \nExcept error: {error} \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['error'] == error, f'\nНекорректная ошибка в теле ответа \nЗапрос : DELETE ' \
            f' \ndata: {data["data_delete"]} \nExcept error: {error} \nResponse: {result} \nResponse body: {result.text}'

    def test_positive_delete_instance(self,api_url, arrange_create_character,data_positive_test):
        """Запросы на удаление экземпляра коллекции с корректными свойствами"""
        create_instance = arrange_create_character(api_url, data=data_positive_test['data_create'])
        result = delete_method(api_url + instance_collection_url+data_positive_test['data_delete'])
        assert create_instance.status_code == 200,f'\nЭкземпляр коллекции для удаления не создан \nЗапрос : POST ' \
            f' \ndata: {data_positive_test["data_create"]} \nResponse: {result} \nResponse body: {result.text}'
        assert result.status_code == 200,f'\nЭкземпляр не удален \nЗапрос : DELETE ' \
            f' \nparams: {data_positive_test["data_delete"]} \nCreate inst data: {create_instance.json()} \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['result']==f'Hero {create_instance.json()["result"]["name"]} is deleted', f'\nНекорректное ' \
            f'тело ответа  \nЗапрос : DELETE \nparams: {data_positive_test["data_delete"]} \nCreate inst data: {create_instance.json()} \nResponse: {result} \nResponse body: {result.text}'
