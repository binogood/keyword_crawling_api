from flask import request, Blueprint
from db_connector import connect_db
from response import *
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from service.rank_service import RankService

class RankView:
    rank_app = Blueprint('rank_dp', __name__, url_prefix='/rank')

    def __init__(self):
        pass

    @rank_app.route('today', methods=['GET'])
    def rank_list():
        connection = None
        NOW = datetime.now()
        T_DAY = (NOW - timedelta(days=1)).date().strftime('%Y-%m-%d')
        YS_DAY = (NOW -timedelta(days=2)).date().strftime('%Y-%m-%d')
        try:
            connection = connect_db()
            rank_service = RankService()
            date_info = {
                'today' : T_DAY,
                'yesterday' : YS_DAY
            }
            rank_list = rank_service.rank_today_service(date_info, connection)

            return rank_list

        except ApiException as e:
            if connection:
                connection.rollback()
            raise e

        finally:
            if connection:
                connection.close()


    @rank_app.route('view', methods=['GET'])
    def homepage_rank():
        connection = None
        NOW = datetime.now()
        T_DAY = (NOW - timedelta(days=1)).date().strftime('%Y-%m-%d')
        YS_DAY = (NOW -timedelta(days=2)).date().strftime('%Y-%m-%d')
        W_DAY = (NOW - timedelta(weeks=1)).date().strftime('%Y-%m-%d')
        M_DAY = (NOW - relativedelta(months=1)).date().strftime('%Y-%m-%d')
        Y_DAY = (NOW - relativedelta(years=1)).date().strftime('%Y-%m-%d')
        try:
            connection = connect_db()
            rank_service = RankService()
            date_info = {
                'today' : T_DAY,
                'yesterday' : YS_DAY,
                'week' : W_DAY,
                'month' : M_DAY,
                'year' : Y_DAY,
            }

            view_list = rank_service.all_view_service(date_info, connection)
            return view_list

        except ApiException as e:
            if connection:
                connection.rollback()
            raise e

        finally:
            if connection:
                connection.close()