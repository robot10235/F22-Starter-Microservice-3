from connection import Connection


class PhoneResource:

    def __int__(self):
        pass

    @staticmethod
    def get_by_uni(uni):
        sql = "SELECT * FROM f22_databases_contacts.phones where guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result

    @staticmethod
    def add_by_uni(uni, data):
        # id is auto increment
        phone_num = data.get('phone_num', '')
        area_code = data.get('area_code', '')
        sql = f'INSERT INTO f22_databases_contacts.phones \
        (guid, phone_num, area_code) \
        VALUES (\'{uni}\', \'{phone_num}\', \'{area_code}\');'
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        conn.commit()
        conn.close()
        return res

    @staticmethod
    def delete_by_uni(uni):
        sql = "DELETE FROM f22_databases_contacts.phones WHERE guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        conn.commit()
        conn.close()
        return res

    # no need for update method
