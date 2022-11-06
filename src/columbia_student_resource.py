from connection import Connection


class StudentResource:

    def __int__(self):
        pass

    @staticmethod
    def add_one(uni, data):
        guid = uni
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        middle_name = data.get('middle_name', '')
        school_code = data.get('school_code', '')
        sql = f'INSERT INTO f22_databases_contacts.students \
        (guid, last_name, first_name, middle_name, school_code) \
        VALUES (\'{guid}\', \'{last_name}\', \'{first_name}\', \'{middle_name}\', \'{school_code}\');'
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        conn.commit()
        conn.close()
        return res

    @staticmethod
    def delete_by_uni(uni):
        sql = "DELETE FROM f22_databases_contacts.students WHERE guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        conn.commit()
        conn.close()
        return res

    @staticmethod
    def get_class():
        sql = "SELECT * FROM f22_databases_contacts.students;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
