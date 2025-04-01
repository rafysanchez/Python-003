# Testes da API de produtos 

import pytest
from app import create_app, db
from app.domain.models.product import Product

@pytest.fixture
def app():
    app = create_app('testing')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_product(client):
    response = client.post('/api/v1/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 99.99,
        'stock': 10
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Product'
    assert data['price'] == 99.99

def test_get_products(client):
    # Create a test product
    client.post('/api/v1/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 99.99,
        'stock': 10
    })
    
    response = client.get('/api/v1/products')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['name'] == 'Test Product'

def test_get_product(client):
    # Create a test product
    create_response = client.post('/api/v1/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 99.99,
        'stock': 10
    })
    product_id = create_response.get_json()['id']
    
    response = client.get(f'/api/v1/products/{product_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Test Product'

def test_update_product(client):
    # Create a test product
    create_response = client.post('/api/v1/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 99.99,
        'stock': 10
    })
    product_id = create_response.get_json()['id']
    
    response = client.put(f'/api/v1/products/{product_id}', json={
        'name': 'Updated Product',
        'description': 'Updated Description',
        'price': 149.99,
        'stock': 20
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Product'
    assert data['price'] == 149.99

def test_delete_product(client):
    # Create a test product
    create_response = client.post('/api/v1/products', json={
        'name': 'Test Product',
        'description': 'Test Description',
        'price': 99.99,
        'stock': 10
    })
    product_id = create_response.get_json()['id']
    
    response = client.delete(f'/api/v1/products/{product_id}')
    assert response.status_code == 204
    
    # Verify product is deleted
    get_response = client.get(f'/api/v1/products/{product_id}')
    assert get_response.status_code == 404 
