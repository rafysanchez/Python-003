# Endpoint de Produtos 

from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.repository.product_repository import ProductRepository
from app.domain.schemas.product_schema import product_schema

bp = Blueprint('products', __name__)
repository = ProductRepository()
service = ProductService(repository)

@bp.route('/products', methods=['GET'])
def get_products():
    products = service.get_all_products()
    return jsonify(products)

@bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = service.get_product(id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

@bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400
    
    product = service.create_product(data)
    return jsonify(product), 201

@bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400
    
    product = service.update_product(id, data)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)

@bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    if service.delete_product(id):
        return '', 204
    return jsonify({'error': 'Product not found'}), 404 
