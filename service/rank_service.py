from flask import jsonify
from response import *

from model.rank_dao import RankDao

class RankService:
    def __init__(self):
        pass

    def rank_today_service(self, date_info, connection):
        rank_dao = RankDao()
        # rank_list = rank_dao.day_rank_dao(date_info ,connection)
        
        # return {'data': rank_list}
        today_rank = rank_dao.day_rank_dao(date_info ,connection)
        print(today_rank)
        yesterday_rank = rank_dao.yesterday_rank_dao(date_info, connection)
        print(yesterday_rank)
        for idx in range(len(today_rank)):
            if today_rank[idx]['name'] == yesterday_rank[idx]['name']:
                today_rank[idx]['change'] = 0
                continue
            elif today_rank[idx]['name'] != yesterday_rank[idx]['name']:
                for jdx in range(len(today_rank)):
                    if today_rank[idx]['name'] == yesterday_rank[jdx]['name']:
                        if today_rank[idx]['rank'] > yesterday_rank[jdx]['rank']:
                            today_rank[idx]['change'] = 2
                        elif today_rank[idx]['rank'] < yesterday_rank[jdx]['rank']:
                            today_rank[idx]['change'] = 1
                        break
                if 'change' not in today_rank[idx]:
                    today_rank[idx]['change'] = 3
        print(today_rank)
        # today_rank_list = {'today':today_rank}
        return {'data':today_rank}
            

    def all_view_service(self, date_info, connection):
        rank_dao = RankDao()
        day_rank = rank_dao.day_rank_dao(date_info ,connection)
        yesterday_rank = rank_dao.yesterday_rank_dao(date_info, connection)
    
        for idx in range(len(day_rank)):
            if day_rank[idx]['name'] == yesterday_rank[idx]['name']:
                day_rank[idx]['change'] = 0
                continue
            elif day_rank[idx]['name'] != yesterday_rank[idx]['name']:
                for jdx in range(len(day_rank)):
                    if day_rank[idx]['name'] == yesterday_rank[jdx]['name']:
                        if day_rank[idx]['rank'] > yesterday_rank[jdx]['rank']:
                            day_rank[idx]['change'] = 2
                        elif day_rank[idx]['rank'] < yesterday_rank[jdx]['rank']:
                            day_rank[idx]['change'] = 1
                        break
                if 'change' not in day_rank[idx]:
                    day_rank[idx]['change'] = 3
                    

        today_rank_list = {'today':day_rank}                
        week_rank_list = {'week' : rank_dao.week_rank_dao(date_info, connection)}
        month_rank_list = {'month' : rank_dao.month_rank_dao(date_info, connection)}
        year_rank_list = {'year' : rank_dao.year_rank_dao(date_info, connection)}

        total_dic = [today_rank_list, week_rank_list, month_rank_list, year_rank_list]
        # total_dic = [week_rank_list, month_rank_list, year_rank_list]
        return {'data': total_dic}
