from connection import Connection


class AddressResource:

    def __int__(self):
        pass

    @staticmethod
    def get_by_uni(uni):
        sql = "SELECT * FROM f22_databases_contacts.addresses where guid=%s;"
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
        street_No = data.get('street_No', '')
        street_name = data.get('street_name', '')
        city = data.get('city', '')
        state = data.get('state', '')
        country_code = data.get('country_code', '')
        postal_code = data.get('postal_code', '')
        sql = f'INSERT INTO f22_databases_contacts.addresses \
        (guid, street_No, street_name, city, state, country_code, postal_code) \
        VALUES (\'{uni}\', \'{street_No}\', \'{street_name}\', \'{city}\', \'{state}\', \'{country_code}\', \'{postal_code}\');'
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        conn.commit()
        conn.close()
        return res

    @staticmethod
    def delete_by_uni(uni):
        sql = "DELETE FROM f22_databases_contacts.addresses WHERE guid=%s;"
        conn = Connection.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uni)
        conn.commit()
        conn.close()
        return res

    # no need for update method
