from Service_req.Base_req import Base_req


class Test_general():

    def test_exist_collection(self,api_url):
        """Проверка существования коллекции /characters"""
        url=api_url+Base_req.collection_url
        result=Base_req.get_method(url)
        assert result.status_code==200,f'Коллекция {Base_req.collection_url} недоступа. \nResponse: {result} \n' \
            f'Response body: {result.text}'
