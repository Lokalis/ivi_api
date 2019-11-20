from Service_req.Base_req import Base_req



class Delete_instance_req():





    @staticmethod
    def delete_instance(api_url,name,auth=None):
        """Метод удаления экземпляра коллекции по свойству name

        Метод составляет валидное имя из переданой строки name
        Валидное имя - если имя указано из нескольких слов - между ними нужно ставить знак +"""
        name = '+'.join(name.split())
        url = f'{api_url}{Base_req.instance_collection_url}?name={name}'
        result = Base_req.delete_method(url, auth=auth)
        return result