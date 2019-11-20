from Service_req.Base_req import Base_req

class Search_instance_req():

    @staticmethod
    def number_items_collection(api_url):
        """Метод возвращает кол-во элементов в коллекции"""
        url=api_url+Base_req.collection_url
        instances=Base_req.get_method(url)
        number_items=len(instances.json()['result'])
        return number_items


    @staticmethod
    def search_instance(api_url, name,auth=None):
        """Метод поиска экземляров коллекции по свойству name

        Метод составитавляет валидное имя из переданой строки name
        Валидное имя - если имя указано из нескольких слов - между ними нужно ставить знак +"""

        name='+'.join(name.split())
        url = f'{api_url}{Base_req.instance_collection_url}?name={name}'
        result=Base_req.get_method(url,auth=auth)
        return result


    @staticmethod
    def date_search_construct(test_case):
        """Функция создания строки запроса данных тест-кейса на поиск экземляра"""
        data='?name='
        if test_case['value'] == 'miss':
            data=''
        else:
            data+=test_case['value']
        return data
