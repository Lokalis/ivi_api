from Service_req.Base_req import Base_req
import random


class Create_instance_req():

    @staticmethod
    def random_characters_data():
        """Метод создания рандомных даных для экземпляра коллекции"""
        data={
            'name':"".join([random.choice('testdefault') for _ in range(random.randint(10, 20))])
        }
        return data


    @staticmethod
    def create_codes(api_url,data='random',auth=None):
        '''Метод создания экземпляра коллекции'''
        url = api_url + Base_req.instance_collection_url
        if data is 'random':
            data=Create_instance_req.random_characters_data()
        result = Base_req.post_method(url, json=data,auth=auth)
        return result

    @staticmethod
    def data_create_construct(test_case, property, data=None):
        """Метод формирует тело запроса исходя из данных тест-кейса"""
        if data is None:
            data = Create_instance_req.random_characters_data()
        if property == 'data':
            data = test_case['value']
            return data
        if test_case['value'] == 'miss':
            del data[property]
        else:
            data[property] = test_case['value']
        if 'add' in test_case:
            for atr in test_case['add']:
                property_atr = atr['attribute']
                data[property_atr] = atr['value']
        return data


    @staticmethod
    def get_test_case(data_test):
        """Метод предоставляет данные для тестирования, сформированные из тест-кейсов"""
        return [tuple([name_property, data_test_case]) for name_property in data_test for data_test_case in
                data_test[name_property]]


    @staticmethod
    def reset_collection(api_url):
        """Метод сбрасывает колекцию в первоначльное состояние"""
        url=api_url+Base_req.reset_collection_url
        result=Base_req.post_method(url)
        return result
