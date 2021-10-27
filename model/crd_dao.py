import pymysql

class CRDDao:
    def __init__(self):
        pass

    # 카테고리 추가
    def create_keyword_dao(self, keyword_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                INSERT INTO keywords (
                    name
                )
                VALUES (
                    %(keyword)s
                )
            """
            cursor.execute(query, keyword_info)
        return cursor.lastrowid 

    # 카테고리 삭제
    def delete_keyword_dao(self, keyword_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                DELETE FROM
                    keywords
                WHERE
                    name = %(keyword)s
            """
            cursor.execute(query, keyword_info)
        return True

    # 카테고리 리스트 출력
    def read_keyword_dao(self, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    name
                FROM
                    keywords
            """
            cursor.execute(query)
        return cursor.fetchall()
    
    # 키워드 있는지 확인
    def find_keyword_dao(self, keyword_info, connection):
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            query = """
                SELECT
                    name
                FROM
                    keywords
                WHERE
                    name = %(keyword)s
            """
            cursor.execute(query, keyword_info)
        return cursor.fetchone()
