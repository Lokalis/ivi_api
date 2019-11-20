from Service_req.Base_req import Base_req
from Service_req.Create_instance_req import Create_instance_req
from Service_req.Search_instance_req import Search_instance_req
from Service_req.Delete_instance_req import Delete_instance_req
from Data_tests import data_search_instance
import pytest


@pytest.mark.skip_api_url_fail
class Test_delete_instance():


    @pytest.mark.parametrize('role,auth,code_except',[('basic',Base_req.auth,400),('invalid auth',('awdawdawd','awd'),401)])
    def test_access_resource_method(self,api_url,code_except,role,auth):
        f"""Выполнение запросов на поиск экземляра коллекции с аутентификацией {role}"""
        search_name='random_name'
        result=Delete_instance_req.delete_instance(api_url,search_name,auth=auth)
        assert result.status_code==code_except,f' Некорректный код ответа на запрос поиска экземпляра с ролью {role}.' \
            f'\nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case',Create_instance_req.get_test_case(data_search_instance.date_negative_search_instance))
    def test_negative_search_instance(self,api_url,arrange_create_character,property,test_case):
        """Запросы на создание экземпляра коллекции с некорректными свойствами"""
        if 'add_instance' in test_case:
            data_create=Create_instance_req.data_create_construct(test_case['add_instance'], property=property)
            arrange_create_character(api_url,data=data_create)
        data_delete = Search_instance_req.data_search_construct(test_case)
        result = Base_req.delete_method(api_url + Base_req.instance_collection_url+data_delete)
        assert result.status_code==400 and result.json()['error']==test_case['error'],f'\nНекорректная ошибка в теле ответа \nЗапрос : DELETE ' \
            f' \ndata: {data_delete} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'


    @pytest.mark.parametrize('property,test_case',Create_instance_req.get_test_case(data_search_instance.data_positive_search_instance))
    def test_positive_search_instance(self,property,test_case,api_url,arrange_create_character):
        """Запросы на создание экземпляра коллекции с корректными свойствами"""
        data_create = Create_instance_req.data_create_construct(test_case['add_instance'], property=property)
        create_instance=arrange_create_character(api_url, data=data_create)
        data_delete = Search_instance_req.data_search_construct(test_case)
        result = Base_req.delete_method(api_url + Base_req.instance_collection_url+data_delete)
        assert create_instance.status_code==200,f'\nЭкземпляр коллекции для удаления не создан \nЗапрос : POST ' \
            f' \ndata: {data_create} \nResponse: {result} \nResponse body: {result.text}'
        assert result.status_code==200 and result.json()['result']==f'Hero {create_instance.json()["result"]["name"]} is deleted',f'\nЭкземпляр не удален \nЗапрос : DELETE ' \
            f' \nparams: {data_delete} \nCreate inst data: {create_instance.json()} \nResponse: {result} \nResponse body: {result.text}'
