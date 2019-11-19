from Service_req.Post_req import Post_req
from Service_req.Base_req import Base_req
from Data_tests import data_post_method
import pytest


@pytest.mark.skip_api_url_fail
class Test_post():



    def test_exist_collection(self,api_url):
        """Проверка существования коллекции /characters"""
        url=api_url+Base_req.collection_url
        result=Base_req.get_method(url)
        assert result.status_code==200,f'Коллекция {Base_req.collection_url} недоступа. \nResponse: {result} \n' \
            f'Response body: {result.text}'


    @pytest.mark.parametrize('role,auth,code_except',[('basic',Base_req.auth,200),('invalid auth',('awdawdawd','awd'),401)])
    def test_access_resource_method(self,api_url,arrange_create_character,role,auth,code_except):
        f"""Выполнение запросов на создание экземляра коллекции с аутентификацией {role}"""
        result=arrange_create_character(api_url,auth=auth)
        assert result.status_code==code_except,f' Некорректный код ответа на запрос создания экземпляра с ролью {role}.' \
            f'\nResponse: {result} \nResponse body: {result.text}'


    @pytest.mark.parametrize('property,test_case',Post_req.get_test_case(data_post_method.data_negative_post))
    def test_negative_create_instance(self,api_url,arrange_create_character,property,test_case):
        """Запросы на создание экземпляра коллекции с некорректными свойствами"""
        data=Post_req.data_construct(test_case,property)
        result=arrange_create_character(api_url,data=data)
        assert result.status_code==400,f'Некорректный код ответа \nЗапрос : POST ' \
            f' \ndata: {data} \nResponse: {result} \nResponse body: {result.text}'
        assert result.json()['error']==test_case['error'],f'Некорректная ошибка в теле ответа \nЗапрос : POST  ' \
            f' \ndata: {data} \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case', Post_req.get_test_case(data_post_method.data_positive_post))
    def test_positive_create_instance(self,api_url,arrange_create_character,property,test_case):
        """Запросы на создание экземпляра коллекции с корректными свойствами"""
        data = Post_req.data_construct(test_case, property)
        result = arrange_create_character(api_url, data=data)
        assert result.status_code==200,f'Экземпляр коллекции не создался\nЗапрос : POST ' \
            f' \ndata: {data} \nResponse: {result} \nResponse body: {result.text}'


    @pytest.mark.parametrize('property,test_case', Post_req.get_test_case(data_post_method.data_duplicate_post))
    def test_duplicate_create_instance(self,api_url,arrange_create_character,property,test_case):
        data_create=Post_req.data_construct(test_case['case_create'],property)
        data_duplicate=Post_req.data_construct(test_case['case_duplicate'],property)
        create_instance=arrange_create_character(api_url,data=data_create)
        duplicate_instance=arrange_create_character(api_url,data=data_duplicate)
        assert create_instance.status_code==200,f'Экземляр-обрзец не создан \nЗапрос : POST ' \
            f' \ndata: {data_create} \nResponse: {create_instance} \nResponse body: {create_instance.text}'
        assert duplicate_instance.status_code==400 and duplicate_instance.json()['error']==f"{test_case['case_create']['value']} is already exists",f'' \
            f'Возникла ошибка при создании дублирующего экземпляра \nЗапрос : POST ' \
            f' \ndata: {data_duplicate} \nResponse: {duplicate_instance} \nResponse body: {duplicate_instance.text}'
