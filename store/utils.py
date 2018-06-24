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
