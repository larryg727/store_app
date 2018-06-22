import mysql.connector
import os

def get_db_settings():
    '''
    Returns DB information
    '''
    return {
        'host' : 'localhost',
        'database': 'storeapp',
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }
