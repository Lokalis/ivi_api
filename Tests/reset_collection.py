from Service_req.Search_instance_req import Search_instance_req
from Service_req.Create_instance_req import Create_instance_req
import pytest

@pytest.mark.skip_api_url_fail
class Test_reset_all_collection():


    def test_reset_collection(self,api_url,arrange_create_character):
        """Проверка работоспособности метода /reset"""
        Create_instance_req.reset_collection(api_url)
        items_collection=Search_instance_req.number_items_collection(api_url)
        arrange_create_character(api_url)
        Create_instance_req.reset_collection(api_url)
        result=Search_instance_req.number_items_collection(api_url)
        assert items_collection==result,f'\nReset не возвращает базу данных к дефолтному виду ' \
            f'\nКол-во элементов после первого reset: {items_collection} \nКол-во элементов после создания экземпляра и ' \
            f'повторного reset: {result}'