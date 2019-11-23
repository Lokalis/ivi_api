from Data_tests.data_create_instance import *
from Service_req.Create_instance_req import *
from Service_req.Search_instance_req import *
import pytest

@pytest.mark.skip_api_url_fail
class Test_create_instance():

    @pytest.fixture(params=get_test_case(data_positive_create))
    def data_positive_test(self,request):
        attribute,test_case=request.param
        data=data_create_construct(test_case,attribute)
        return data

    @pytest.fixture(params=get_test_case(data_negative_create))
    def data_negative_test(self, request):
        attribute, test_case = request.param
        data = data_create_construct(test_case, attribute)
        return data,test_case['error']

    @pytest.fixture(params=get_test_case(data_duplicate_create))
    def data_duplicate_test(self, request):
        attribute, test_case = request.param
        data_create = data_create_construct(test_case['case_create'], attribute)
        data_duplicate=data_create_construct(test_case['case_duplicate'], attribute)
        return data_create,data_duplicate

    @pytest.mark.parametrize('role,auth,code_except', [('basic', None, 200), ('invalid full auth', ('awdawdawd', 'awd'), 401),('invalid email',('den','hgJH768Cv23'),401)])
    def test_access_resource_method(self, api_url, arrange_create_character, role, auth, code_except):
        f"""Выполнение запросов на создание экземляра коллекции с аутентификацией {role}"""
        result = arrange_create_character(api_url, auth=auth)
        assert result.status_code == code_except, f'\nНекорректный код ответа на запрос создания экземпляра с ' \
            f'aутентификацией {role} \nAuth: {auth} \nЗапрос: POST \nExcept code: {code_except}\nResponse: {result} ' \
            f'\nResponse body: {result.text}'


    def test_negative_create_instance(self, api_url, arrange_create_character,data_negative_test):
        """Запросы на создание экземпляра коллекции с некорректными свойствами"""
        data,error=data_negative_test
        result = arrange_create_character(api_url, data=data)
        assert result.status_code == 400 ,f'\nНекорректный код ответа \nЗапрос : POST  ' \
            f' \ndata: {data} \nExcept error: {error} \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['error'] == error, f'\nНекорректная ошибка в теле ответа \nЗапрос : POST  ' \
            f' \ndata: {data} \nExcept error: {error} \nResponse: {result} \nResponse body: {result.text}'

    def test_positive_create_instance(self, api_url, arrange_create_character,data_positive_test):
        """Запросы на создание экземпляра коллекции с корректными свойствами"""
        result = arrange_create_character(api_url, data=data_positive_test)
        assert result.status_code == 200, f'\nЭкземпляр коллекции не создался \nЗапрос : POST ' \
            f' \ndata: {data_positive_test} \nResponse: {result} \nResponse body: {result.text}'

    def test_duplicate_create_instance(self, api_url, arrange_create_character, data_duplicate_test):
        """Запросы на создание экземпляра коллекции с дублирующими свойствами"""
        data_create,data_duplicate=data_duplicate_test
        create_instance = arrange_create_character(api_url, data=data_create)
        duplicate_instance = arrange_create_character(api_url, data=data_duplicate)
        assert create_instance.status_code == 200, f'\nЭкземляр-образец не создан \nЗапрос : POST ' \
            f' \ndata: {data_create} \nResponse: {create_instance} \nResponse body: {create_instance.text}'
        assert duplicate_instance.status_code == 400,f'\nВозникла ошибка при создании дублирующего экземпляра \nЗапрос : POST ' \
            f' \ndata: {data_duplicate} \nExcept error: 400 \nResponse: {duplicate_instance} \nResponse body: {duplicate_instance.text}'
        assert duplicate_instance.json()['error'] == f"{data_create['name']} is already exists",f'' \
            f'\nНекорректная ошибка в теле ответа \nЗапрос : POST \ndata: {data_duplicate} \nExcept error: {data_create["name"]} is already exists \nResponse: {duplicate_instance} \nResponse body: {duplicate_instance.text}'

    def test_creation_limit_instance(self, api_url):
        """Серия запросов на создание экземпляров для тестирования ситуации переполнености базы"""
        items_now = number_items_collection(api_url)
        for instance in range(max_items_collections-items_now):
            create_character(api_url)
        result = create_character(api_url)
        assert result.status_code == 400,f'\nНекорректный код ответа \nЗапрос : POST \ndata: random \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['error'] == "Collection can't contain more than 500 items", f'\nБаза данных вмещает больше чем 500 персонажей'
