import os

class Config:
    ENV = os.getenv('ENVIRONMENT')

    def __init__(self):
        if self.ENV == 'dev':
            self.base_url = 'http://localhost:5000'
            self.allowed_url = 'http://localhost:3000'
            self.db_host = '<LOCAL_DBHOST>
            self.db_name = '<LOCAL_DB_NAME>'
            self.db_user = '<LOCAL_DB_USER>'
            self.db_password = '<LOCAL_DB_PASSWORD'
        elif self.ENV == 'production':
            self.base_url = '<BACKEND_URL>'
            self.allowed_url = '<FRONTEND_URL>'
            self.db_host = '<SERVER_DBHOST>'
            self.db_name = '<SERVER_DB_NAME>'
            self.db_user = '<SERVER_DB_USER>'
            self.db_password = '<SERVER_DB_PASSWORD>'
