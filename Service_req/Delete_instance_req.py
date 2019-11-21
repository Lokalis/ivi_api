from Service_req.Base_req import Base_req


class Delete_instance_req(Base_req):

    def delete_instance(self, api_url, name, auth=None):
        """Метод удаления экземпляра коллекции по свойству name

        Метод составляет валидное имя из переданой строки name
        Валидное имя - если имя указано из нескольких слов - между ними нужно ставить знак +"""
        name = '+'.join(name.split())
        url = f'{api_url}{self.app.instance_collection_url}?name={name}'
        result = self.delete_method(url, auth=auth)
        return result