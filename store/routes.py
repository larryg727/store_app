from flask import jsonify, request
from store import app

from store import utils
from store import data_service


@app.route('/api/add/product', methods=['POST'])
def create_product():
    '''
    Creates product and saves to DB
    '''

    product_id = data_service.save_new_product(request.form)
    print(product_id)
    return 'true', 200


@app.route('/api/products')
def get_products():
    '''
    Returns list of products
    '''
    print(request.headers)
    products = data_service.get_all_products()
    final_products = utils.prepare_product_data_for_return(products)

    return jsonify(final_products), 200
