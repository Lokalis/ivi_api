from Service_req.Base_req import Base_req


class Modify_req(Base_req):

    def modify_instance(self, api_url, data, auth=None):
        """Метод изменения экземпляра на основании переданных данных data"""
        url = api_url+self.app.instance_collection_url
        result = self.put_method(url,json=data,auth=auth)
        return result

    def modify_data_construct(self, property, test_case, name):
        """Метод подготовки данных из тест-кейса"""
        data_default = {
            'name': name
        }
        data_modify = self.app.Create_instance_req.data_create_construct(property=property, test_case=test_case, data=data_default)
        return data_modify
