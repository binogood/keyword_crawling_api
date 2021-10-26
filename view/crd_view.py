from flask import request, Blueprint
from db_connector import connect_db
from model import crd_dao
from response import *

from service.crd_service import CRDService


class CRDView:
    crd_app = Blueprint('crd_dp', __name__, url_prefix='/crd')

    def __init__(self):
        pass

    @crd_app.route('create', methods=['POST'])
    def create_keyword():
        connection = None
        data = request.json
        if 'keyword' not in data:
            raise ApiException(400, INVALID_INPUT_KEYWORD)

        keyword_info = {
            'keyword' : data['keyword'],
        }
        connection = connect_db()
        keyword_service = CRDService()

        new_keyword = keyword_service.create_keyword_service(keyword_info, connection)
        if not new_keyword:
            raise ApiException(400, ALREADY_EXISTS_KEYWORD)
        
        connection.commit()
        return {"message": "CREATE_KEYWORD"}
        

    @crd_app.route('delete', methods=['POST'])
    def delete_keyword():
        connection = None
        data = request.json
        if 'keyword' not in data:
            raise ApiException(400, INVALID_INPUT_KEYWORD)

        keyword_info = {
            'keyword' : data['keyword'],
        }
        connection = connect_db()
        keyword_service = CRDService()

        keyword_service.del_keyword_service(keyword_info, connection)
        connection.commit()
        return {"message": "DELETE_KEYWORD"}

    @crd_app.route('list', methods=['GET'])
    def read_keyword():
        connection = None
        connection = connect_db()
        keyword_service = CRDService()

        keyword_list = keyword_service.read_keyword_service(connection)
        return keyword_list