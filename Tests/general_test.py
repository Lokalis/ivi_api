import pytest
from Service_req.Base_req import *

@pytest.mark.skip_api_url_fail
class Test_general():

    def test_exist_collection(self, api_url):
        """Проверка существования коллекции /characters"""
        url = api_url+collection_url
        result = get_method(url)
        assert result.status_code == 200,f'\nКоллекция {collection_url} недоступа. \nResponse: {result} \n' \
            f'Response body: {result.text}'
