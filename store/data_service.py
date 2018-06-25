from store import utils


def save_new_product(formData):
    '''
    Returns id of product after saving to DB
    '''
    name = formData.get('name')
    description = formData.get('description')
    price = formData.get('price')
    db = utils.get_db_instance()
    cur = db.cursor()
    query = f'INSERT INTO products (name, description, price) VALUES ("{name}", "{description}", "{price}");'
    cur.execute(query)
    last_id = cur.lastrowid
    db.commit()

    cur.close()
    db.close()

    return last_id


def get_all_products():
    '''
    Returns all products in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor()
    cur.execute(
        'SELECT name, description, price FROM products;')
    products = cur.fetchall()

    cur.close()
    db.close()

    return products
