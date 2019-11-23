from Service_req.Modify_instance_req import *
from Data_tests.data_create_instance import data_negative_create
from Data_tests.data_modify_instance import *
import pytest

@pytest.mark.skip_api_url_fail
class Test_modify_instance():

    @pytest.fixture(params=get_test_case(data_positive_modify))
    def data_positive_test(self,request):
        attribute, test_case = request.param
        return attribute,test_case

    @pytest.fixture(params=get_test_case(data_negative_create))
    def data_negative_test(self, request):
        attribute,test_case = request.param
        return attribute,test_case

    @pytest.mark.parametrize('role,auth,code_except', [('basic', None, 400), ('invalid auth', ('awdawdawd', 'awd'), 401),('invalid email',('den','hgJH768Cv23'),401)])
    def test_access_resource_method(self, api_url, arrange_create_character, role, auth, code_except):
        f"""Выполнение запросов на создание экземляра коллекции с аутентификацией {role}"""
        unknown_instance = {'name': 'test_access_resource'}
        result = modify_instance(api_url, unknown_instance, auth=auth)
        assert result.status_code == code_except, f'\nНекорректный код ответа на запрос создания экземпляра с ' \
            f'aутентификацией {role} \nAuth: {auth} \nЗапрос: PUT \nResponse: {result} \nResponse body: {result.text}'

    def test_positive_modify_instance(self, api_url, arrange_create_character, data_positive_test):
        """Запросы на изменение экземпляра с корректными параметрами"""
        attribute,test_case=data_positive_test
        data_modify = modify_data_construct(attribute,test_case,arrange_create_character(api_url).json()['result']['name'])
        result = modify_instance(api_url, data_modify)
        assert result.status_code == 200, f'\nЭкземпляр коллекции не изменился \nЗапрос : PUT ' \
            f'\ndata: {data_modify} \nResponse: {result} \nResponse body: {result.text}'

    def test_negative_modify_instance(self,api_url, arrange_create_character, data_negative_test):
        """Запросы на изменение экземпляра с корректными параметрами"""
        attribute,test_case=data_negative_test
        data_modify = modify_data_construct(attribute, test_case,arrange_create_character(api_url).json()['result']['name'])
        result = modify_instance(api_url, data_modify)
        assert result.status_code==400, f'\nНекорректный код ответа \nЗапрос : PUT  ' \
            f' \ndata: {data_modify} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['error'] == test_case['error'], f'\nНекорректная ошибка в теле ответа \nЗапрос : PUT  ' \
            f' \ndata: {data_modify} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'