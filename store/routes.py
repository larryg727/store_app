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
    categories = data_service.get_all_categories()
    subcategories = data_service.get_all_subcategories()
    json = {'products': products, 'categories': categories,
            'subcategories': subcategories}
    return jsonify(json), 200


@app.route('/api/update/product/<product_id>', methods=['POST'])
def update_product(product_id):
    '''
    updates product by id
    '''
    result = data_service.update_product(request.form, product_id)
    json = {'result': str(result)}
    return jsonify(json), 200


@app.route('/api/categories')
def get_categories():
    '''
    Returns a list of all categories
    '''
    categories = data_service.get_all_categories()
    json = {'categories': categories}
    return jsonify(json), 200


@app.route('/api/add/category', methods=['POST'])
def create_category():
    '''
    Creates new Category
    '''
    result = data_service.save_new_category(request.form)
    json = {'result': str(result)}
    return jsonify(json), 200


@app.route('/api/products/<category>')
def get_products_by_category(category):
    '''
    Returns all products from category
    '''
    products = data_service.all_by_category(category)
    json = {'products': products}
    return jsonify(json), 200


@app.route('/api/add/subcategory', methods=['POST'])
def create_subcategory():
    '''
    Creates new subcategory
    '''
    result = data_service.save_new_subcategory(request.form)
    json = {'result': str(result)}
    return jsonify(json), 200
