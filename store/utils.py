import mysql.connector
import os
from config import Config

def get_db_instance():
    '''
    Returns db instance
    '''
    database_config = Config()
    db = mysql.connector.connect(host=database_config.db_host,
                                 user=database_config.db_user,
                                 database=database_config.db_name,
                                 password=database_config.db_password)
    return db
