from flask import jsonify, request
from store.store_app import app

from store import utils
from store import data_service


@app.route('/api/add/product', methods=['POST'])
def create_product():
    '''
    Creates product and saves to DB
    '''

    result = data_service.save_new_product(request.form)
    json = {'result': str(result)}
    return jsonify(json), 200


@app.route('/api/products')
def get_products():
    '''
    Returns list of products
    '''
    products = data_service.get_all_products()
    print(products)
    return jsonify(products), 200
