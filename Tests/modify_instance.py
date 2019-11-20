from Service_req.Create_instance_req import Create_instance_req
from Service_req.Base_req import Base_req
from Data_tests import data_create_instance
from Service_req.Modify_req import Modify_req
from Data_tests import data_modify_instance
import pytest


@pytest.mark.skip_api_url_fail
class Test_create_instance():


    @pytest.mark.parametrize('role,auth,code_except',[('basic',Base_req.auth,400),('invalid auth',('awdawdawd','awd'),401)])
    def test_access_resource_method(self,api_url,arrange_create_character,role,auth,code_except):
        f"""Выполнение запросов на создание экземляра коллекции с аутентификацией {role}"""
        unknown_instance={'name':'test_access_resource'}
        result=Modify_req.modify_instance(api_url,unknown_instance,auth=auth)
        assert result.status_code==code_except,f' Некорректный код ответа на запрос создания экземпляра с ролью {role}.' \
            f'\nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case',Create_instance_req.get_test_case(data_modify_instance.data_positive_modify))
    def test_positive_modify_instance(self,api_url,property,test_case,arrange_create_character):
        """Запросы на изменение экземпляра с корректными параметрами"""
        data_modify=Modify_req.modify_data_construct(property,test_case,arrange_create_character(api_url).json()['result']['name'])
        result=Modify_req.modify_instance(api_url,data_modify)
        assert result.status_code==200,f'Экземпляр коллекции не изменился \nЗапрос : POST ' \
            f' \ndata: {data_modify} \nResponse: {result} \nResponse body: {result.text}'

    @pytest.mark.parametrize('property,test_case',
                             Create_instance_req.get_test_case(data_create_instance.data_negative_create))
    def test_negative_modify_instance(self,property,test_case,api_url,arrange_create_character):
        data_modify = Modify_req.modify_data_construct(property, test_case,
                                                       arrange_create_character(api_url).json()['result']['name'])
        result = Modify_req.modify_instance(api_url, data_modify)
        assert result.status_code==400 and result.json()['error']==test_case['error'],f'\nНекорректная ошибка в теле ответа \nЗапрос : POST  ' \
            f' \ndata: {data_modify} \nExcept error: {test_case["error"]} \nResponse: {result} \nResponse body: {result.text}'