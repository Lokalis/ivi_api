from Service_req.Base_req import Base_req
from Service_req.Create_instance_req import Create_instance_req



class Modify_req():


    @staticmethod
    def modify_instance(api_url,data,auth=None):
        url=api_url+Base_req.instance_collection_url
        result=Base_req.put_method(url,json=data,auth=auth)
        return result


    @staticmethod
    def modify_data_construct(property,test_case,name):
        data_default={
            'name':name
        }
        data_modify=Create_instance_req.data_create_construct(property=property,test_case=test_case,data=data_default)
        return data_modify