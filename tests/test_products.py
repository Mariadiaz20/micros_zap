from fastapi.testclient import TestClient
from app.main import app
from app.schemas.schemas import ProductoCreate, Producto
from app.models.models import Producto as ProductoModel  # Assuming the ORM model is defined here
from app.db.session import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

def test_create_producto():
    producto_data = {
        "nombre": "Test Producto",
        "descripcion": "Descripción del producto de prueba",
        "precio": 10.99,
        "stock": 100,
        "imagen_url": "http://example.com/image.png",
        "categoria_id": 1  # Assuming a category with ID 1 exists
    }
    response = client.post("/productos/", json=producto_data)
    assert response.status_code == 201
    created_producto = response.json()
    assert created_producto["nombre"] == producto_data["nombre"]
    assert created_producto["precio"] == producto_data["precio"]

def test_read_producto():
    response = client.get("/productos/1")  # Assuming a product with ID 1 exists
    assert response.status_code == 200
    producto = response.json()
    assert producto["id"] == 1

def test_update_producto():
    producto_data = {
        "nombre": "Updated Producto",
        "precio": 12.99
    }
    response = client.put("/productos/1", json=producto_data)  # Assuming a product with ID 1 exists
    assert response.status_code == 200
    updated_producto = response.json()
    assert updated_producto["nombre"] == producto_data["nombre"]
    assert updated_producto["precio"] == producto_data["precio"]

def test_delete_producto():
    response = client.delete("/productos/1")  # Assuming a product with ID 1 exists
    assert response.status_code == 204
    response = client.get("/productos/1")
    assert response.status_code == 404  # Product should no longer exist