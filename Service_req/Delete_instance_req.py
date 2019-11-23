from Service_req.Base_req import *


def delete_instance(api_url, name, auth=None):
    """Метод удаления экземпляра коллекции по свойству name

    Метод составляет валидное имя из переданой строки name
    Валидное имя - если имя указано из нескольких слов - между ними нужно ставить знак +"""
    name = '+'.join(name.split())
    url = f'{api_url}{instance_collection_url}?name={name}'
    result = delete_method(url, auth=auth)
    return result