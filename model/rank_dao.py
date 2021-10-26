import pymysql


class RankDao:
    def __init__(self):
        pass

    # 일 랭킹
    def day_rank_dao(self, date_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query ="""
                SELECT
                    r.rank,
                    k.name,
                    r.count
                FROM
                    ranking r
                INNER JOIN
                    keywords k
                    ON k.id = r.keyword_id
                WHERE
                    DATE(date) = %(today)s and r.rank <= 10
                ORDER BY 
                    r.rank
            """ 
            cursor.execute(query, date_info)
        return cursor.fetchall()

    # 어제 랭킹
    def yesterday_rank_dao(self, date_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    r.rank,
                    k.name
                FROM
                    ranking r
                INNER JOIN
                    keywords k
                    ON k.id = r.keyword_id
                WHERE
                    DATE(date) = %(yesterday)s and r.rank <= 10
                ORDER BY 
                    r.rank
            """
            cursor.execute(query, date_info)
        return cursor.fetchall()

    # 주 랭킹
    def week_rank_dao(self, date_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    r.rank,
                    r.date,
                    k.name
                FROM
                    ranking r
                INNER JOIN
                    keywords k
                    ON k.id = r.keyword_id
                WHERE
                    DATE(date) between %(week)s and %(today)s and r.rank <= 10
                ORDER BY 
                    r.date,
                    r.rank

            """
            cursor.execute(query, date_info)
        return cursor.fetchall()

    # 월 랭킹
    def month_rank_dao(self, date_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    wr.date,
                    wr.rank,
                    k.name
                FROM
                    week_ranking wr
                INNER JOIN
                    keywords k
                    ON k.id = wr.keyword_id
                WHERE
                    DATE(date) between %(month)s and %(today)s and wr.rank <= 10
                ORDER BY 
                    wr.date,
                    wr.rank
            """
            cursor.execute(query, date_info)
        return cursor.fetchall()

    # 연 랭킹
    def year_rank_dao(self, date_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    wr.date,
                    wr.rank,
                    k.name
                FROM
                    week_ranking wr
                INNER JOIN
                    keywords k
                    ON k.id = wr.keyword_id
                WHERE
                    DATE(date) between %(year)s and %(today)s and wr.rank <= 10
                ORDER BY 
                    wr.date,
                    wr.rank
            """
            cursor.execute(query, date_info)
        return cursor.fetchall()

