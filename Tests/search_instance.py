from Service_req.Base_req import Base_req
from Service_req.Create_instance_req import Post_req
import pytest

class Test_search_instance():



    @pytest.mark.parametrize('role,auth,code_except',[('basic',Base_req.auth,200),('invalid auth',('awdawdawd','awd'),401)])
    def test_access_resource_method(self,auth,code_except):
        f"""Выполнение запросов на поиск экземляра коллекции с аутентификацией {role}"""
        result=arrange_create_character(api_url,auth=auth)
        assert result.status_code==code_except,f' Некорректный код ответа на запрос создания экземпляра с ролью {role}.' \
            f'\nResponse: {result} \nResponse body: {result.text}'