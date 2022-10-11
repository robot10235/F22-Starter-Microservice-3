from connection import Connection


class MailResource:

    def __int__(self):
        pass

    @staticmethod
    def get_by_uni(uni):
        sql = "SELECT * FROM f22_databases_contacts.emails where guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        result = cur.fetchone()
        conn.commit()
        conn.close()
        return result

    @staticmethod
    def add_by_uni(uni, data):
        # id is auto increment
        email = data.get('email_address', '')
        sql = f'INSERT INTO f22_databases_contacts.emails \
        (guid, email_address) \
        VALUES (\'{uni}\', \'{email}\');'
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        conn.commit()
        conn.close()
        return res

    @staticmethod
    def delete_by_uni(uni):
        sql = "DELETE FROM f22_databases_contacts.emails WHERE guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        conn.commit()
        conn.close()
        return res

    # no need for update method
