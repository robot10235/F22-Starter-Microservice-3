from connection import Connection
import requests


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
        county_code = data.get('county_code', '')
        postal_code = data.get('postal_code', '')
        sql = f'INSERT INTO f22_databases_contacts.addresses \
        (guid, street_No, street_name, city, state, county_code, postal_code) \
        VALUES (\'{uni}\', \'{street_No}\', \'{street_name}\', \'{city}\', \'{state}\', \'{county_code}\', \'{postal_code}\');'
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

    @staticmethod
    def is_valid_address(data):
        street_No = data.get('street_No', '')
        street_name = data.get('street_name', '')
        city = data.get('city', '')
        state = data.get('state', '')
        country_code = data.get('country_code', '')
        postal_code = data.get('postal_code', '')
        url = 'https://us-street.api.smartystreets.com/street-address?' \
              'auth-id=62b1879c-1836-d927-abad-019dc07b5b50&auth-token=7DwB3e0r3XBuDRdb4KLK' \
              f'&street={street_No} {street_name}' \
              f'&city={city}' \
              f'&state={state}' \
              f'&zipcode={postal_code}'
        res = requests.get(url)
        return res != '[]'
    # no need for update method
