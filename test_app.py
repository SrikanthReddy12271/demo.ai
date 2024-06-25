import pytest
from flask import Flask
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Arithmetic Calculator' in response.data

def test_add(client):
    response = client.post('/add', data={'num1': '2', 'num2': '3'})
    assert response.status_code == 200
    assert b'The result is: 5' in response.data

def test_subtract(client):
    response = client.post('/subtract', data={'num1': '5', 'num2': '2'})
    assert response.status_code == 200
    assert b'The result is: 3' in response.data

def test_multiply(client):
    response = client.post('/multiply', data={'num1': '4', 'num2': '6'})
    assert response.status_code == 200
    assert b'The result is: 24' in response.data

def test_divide(client):
    response = client.post('/divide', data={'num1': '10', 'num2': '2'})
    assert response.status_code == 200
    assert b'The result is: 5.0' in response.data

def test_division_by_zero(client):
    response = client.post('/divide', data={'num1': '10', 'num2': '0'})
    assert response.status_code == 200
    assert b'Error: Division by zero' in response.data