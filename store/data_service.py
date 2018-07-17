from store import utils
from store.product import Product


def save_new_product(formData):
    '''
    Takes in form data and creates product instance and saves it.
    '''
    name = formData.get('name')
    description = formData.get('description')
    price = formData.get('price')
    category_id = formData.get('category')
    new_product = Product(name, description, price)
    new_product.save()
    result = False
    if new_product.is_persisted():
        result = add_product_category(category_id, new_product.id)

    return result


def get_all_products():
    '''
    Returns all products in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor(dictionary=True)
    cur.execute(
        'SELECT * FROM products;')
    products = cur.fetchall()

    cur.close()
    db.close()

    return products


def get_all_categories():
    '''
    Returns all categories in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor(dictionary=True)
    cur.execute(
        'SELECT * FROM category;')
    categories = cur.fetchall()

    cur.close()
    db.close()

    return categories

def save_new_category(formData):
    '''
    Takes in form data and saves new category
    '''
    name = formData.get('name')

    db = utils.get_db_instance()
    cursor = db.cursor()
    query = f'INSERT INTO category (name) VALUES ("{name}");'
    cursor.execute(query)

    last_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()

    return type(last_id) is int

def all_by_category(category):
    '''
    Returns all products from db from category
    '''
    db = utils.get_db_instance()
    cursor = db.cursor(dictionary=True)
    query = f'SELECT * FROM products LEFT JOIN product_category ON products.id = product_category.product_id WHERE product_category.category_id = {category};'
    cursor.execute(query)
    products = cursor.fetchall()
    
    cursor.close()
    db.close()
    print(products)
    return products

def add_product_category(category_id, product_id):
    '''
    Saves product category in db
    '''
    db = utils.get_db_instance()
    cursor = db.cursor()
    query = f'INSERT INTO product_category (category_id, product_id) VALUES ({category_id}, {product_id});'
    cursor.execute(query)
    
    last_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()

    return type(last_id) is int
    