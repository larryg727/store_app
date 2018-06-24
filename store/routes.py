from flask import jsonify, request
from store import app

from store import utils


@app.route('/product/create', methods=['POST'])
def create_product():
    '''
    Creates product and saves to DB
    '''
    name = request.form.get('name')
    description = request.form.get('description')
    price = request.form.get('price')
    db = utils.get_db_instance()
    cur = db.cursor()
    query = f'INSERT INTO products (name, description, price) VALUES ("{name}", "{description}", "{price}");'
    print(query)
    cur.execute(query)
    last_id = cur.lastrowid
    db.commit()

    cur.close()
    db.close()
    
    return 'true', 200


@app.route('/products')
def get_products():
    '''
    Returns list of products
    '''
    db = utils.get_db_instance()
    cur = db.cursor()
    cur.execute(
        'SELECT name, description, price FROM products;')
    products = cur.fetchall()
    final_products = []
    for prod in products:
        new_product = {
            'name': prod[0],
            'description': prod[1],
            'price': prod[2]
        }
        final_products.append(new_product)

    cur.close()
    db.close()
    return jsonify(final_products), 200
