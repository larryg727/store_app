import mysql.connector
import os


def get_db_settings():
    '''
    Returns DB information
    '''
    return {
        'host': 'localhost',
        'database': 'storeapp',
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }


def get_db_instance():
    '''
    Returns db instance
    '''
    database = get_db_settings()
    db = mysql.connector.connect(host=database['host'],
                                 user=database['user'],
                                 database=database['database'],
                                 password=database['password'])
    return db

def prepare_product_data_for_return(data):
    '''
    Returns db data with keys for values
    '''
    final_products = []
    for prod in data:
        new_product = {
            'name': prod[0],
            'description': prod[1],
            'price': prod[2]
        }
        final_products.append(new_product)
    return final_products