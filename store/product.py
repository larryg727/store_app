from store import utils


class Product:

    def __init__(self, name, description, price, details, category_id, subcategory_id):
        self.name = name
        self.description = description
        self.price = price
        self.details = details
        self.category_id = category_id
        self.subcategory_id = subcategory_id
        self.id = None

    def save(self):
        '''
        Saves instance of Product to DB and adds DB id to instance
        '''
        db = utils.get_db_instance()
        cursor = db.cursor()

        query = f'INSERT INTO products (name, description, details, price, category_id, subcategory_id) VALUES ("{self.name}", "{self.description}", "{self.details}", {self.price}, {self.category_id}, {self.subcategory_id});'
        cursor.execute(query)

        last_id = cursor.lastrowid
        db.commit()

        cursor.close()
        db.close()

        self.id = last_id

        return self

    def is_persisted(self):
        '''
        Method checks to see if DB id has been assinged to instance
        '''
        if self.id is not None:
            return True
        else:
            return False
