from store import utils
from store.product import Product


def save_new_product(formData):
    '''
    Takes in form data and creates product instance and saves it.
    '''
    name = formData.get('name')
    description = formData.get('description')
    price = formData.get('price')
    details = formData.get('details')
    category_id = formData.get('category') if formData.get(
        'category') != '' else 'NULL'
    subcategory_id = formData.get('subcategory') if formData.get(
        'subcategory') != '' else 'NULL'
    new_product = Product(name, description, price,
                          details, category_id, subcategory_id)
    new_product.save()

    return new_product.is_persisted()


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


def update_product(formData, product_id):
    '''
    Updates product in db
    '''
    name = formData.get('name')
    description = formData.get('description')
    price = formData.get('price')
    details = formData.get('details')
    category_id = formData.get('category') if formData.get(
        'category') != '' else 'NULL'
    subcategory_id = formData.get('subcategory') if formData.get(
        'subcategory') != '' else 'NULL'
    product = Product(name, description, price,
                          details, category_id, subcategory_id)
    product.update_product(product_id)

    return True


def get_all_categories():
    '''
    Returns all categories in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor(dictionary=True)
    cur.execute(
        'SELECT * FROM categories;')
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
    query = f'INSERT INTO categories (name) VALUES ("{name}");'
    cursor.execute(query)

    last_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()

    if type(last_id) is int:
        return last_id
    else:
        return False


def all_by_category(category):
    '''
    Returns all products from db from category
    '''
    db = utils.get_db_instance()
    cursor = db.cursor(dictionary=True)
    # query = f'SELECT * FROM products LEFT JOIN categories ON products.id = categories.id WHERE products.category_id = {category};'
    query = f'SELECT products.name as name, products.description, products.details, products.price, subcategories.name as subcategory FROM products LEFT JOIN subcategories ON products.subcategory_id = subcategories.id WHERE products.category_id = {category};'
    cursor.execute(query)
    products = cursor.fetchall()

    cursor.close()
    db.close()
    
    return products


def save_new_subcategory(formData):
    '''
    Takes in form data and saves new category
    '''
    name = formData.get('name')
    category_id = formData.get('category')

    db = utils.get_db_instance()
    cursor = db.cursor()
    query = f'INSERT INTO subcategories (name, category_id) VALUES ("{name}", {category_id});'
    cursor.execute(query)

    last_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()

    if type(last_id) is int:
        return last_id
    else:
        return False


def get_all_subcategories():
    '''
    Returns all categories in DB
    '''
    db = utils.get_db_instance()
    cur = db.cursor(dictionary=True)
    cur.execute(
        'SELECT * FROM subcategories;')
    subcategories = cur.fetchall()

    cur.close()
    db.close()

    return subcategories


def save_to_db(query):
    '''
    Generic method to save to db by query
    '''
    db = utils.get_db_instance()
    cursor = db.cursor()
    cursor.execute(query)

    last_id = cursor.lastrowid
    db.commit()
    cursor.close()
    db.close()

    if type(last_id) is int:
        return last_id
    else:
        return False
