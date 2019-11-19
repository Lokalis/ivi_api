from Service_req.Create_instance_req import Post_req
from Service_req.Base_req import Base_req
from Data_tests import data_post_method
from Service_req.Search_instance_req import Get_req
import pytest


@pytest.mark.skip_api_url_fail
class Test_create_instance():


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
        assert result.status_code==400 and result.json()['error']==test_case['error'],f'Некорректная ошибка в теле ответа \nЗапрос : POST  ' \
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


    def test_creation_limit_instance(self,api_url):
        items_now=Get_req.number_items_collection(api_url)
        for instance in range(Base_req.max_items_collections-items_now):
            Post_req.create_codes(api_url)
        result=Post_req.create_codes(api_url)
        assert result.status_code==400 and result.json()['error']=="Collection can't contain more than 500 items",f'База данных вмещает больше чем 500 персонажей'