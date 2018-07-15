from store import utils
from store.product import Product


def save_new_product(formData):
    '''
    Returns id of product after saving to DB
    '''
    name = formData.get('name')
    description = formData.get('description')
    price = formData.get('price')
    new_product = Product(name, description, price)
    new_product.save()
    return new_product.isPersisted()


def get_all_products():
    '''
    Returns all products in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor(dictionary=True)
    cur.execute(
        'SELECT name, description, price FROM products;')
    products = cur.fetchall()

    cur.close()
    db.close()

    return products
