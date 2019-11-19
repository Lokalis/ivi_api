from Service_req.Base_req import Base_req

class Get_req():

    @staticmethod
    def number_items_collection(api_url):
        url=api_url+Base_req.collection_url
        instances=Base_req.get_method(url)
        number_items=len(instances.json()['result'])
        return number_items