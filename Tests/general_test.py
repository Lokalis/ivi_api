import pytest

@pytest.mark.skip_api_url_fail
class Test_general():

    def test_exist_collection(self, api_url, client):
        """Проверка существования коллекции /characters"""
        url = api_url+client.collection_url
        result = client.Base_req.get_method(url)
        assert result.status_code == 200,f'\nКоллекция {client.collection_url} недоступа. \nResponse: {result} \n' \
            f'Response body: {result.text}'
