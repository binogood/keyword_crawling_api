from model.crd_dao import CRDDao
from flask import jsonify
from response import *

class CRDService:
    def __init__(self):
        pass

    def create_keyword_service(self, keyword_info, connection):
        create_dao = CRDDao()
        create_keyword = create_dao.find_keyword_dao(keyword_info, connection)
        if create_keyword:
            raise ApiException(400, DUPLICATED_KEYWORD)

        new_keyword = create_dao.create_keyword_dao(keyword_info, connection)
        return new_keyword 

    def del_keyword_service(self, keyword_info, connection):
        delete_dao = CRDDao()
        delete_keyword = delete_dao.find_keyword_dao(keyword_info, connection)
        if not delete_keyword:
            raise ApiException(400, FIND_NOT_KEYWORD)
            
        delete_dao.delete_keyword_dao(keyword_info, connection)
        return True

    def read_keyword_service(self, connection):
        read_dao = CRDDao()
        read_keyword = read_dao.read_keyword_dao(connection)
        return {'data' : read_keyword}
        