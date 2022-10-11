import pymysql
import os


class Connection:

    def __int__(self):
        pass

    @staticmethod
    def get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            # user="root",
            # password="123456",
            # host="localhost",
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn
