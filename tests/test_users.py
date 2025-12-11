from fastapi.testclient import TestClient
from app.main import app
from app.schemas.schemas import UsuarioCreate, Usuario
from app.services.user_service import create_user

client = TestClient(app)

def test_create_user():
    user_data = {
        "nombre": "Test User",
        "email": "testuser@example.com",
        "telefono": "1234567890",
        "password": "securepassword"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["nombre"] == user_data["nombre"]
    assert created_user["email"] == user_data["email"]
    assert "id" in created_user

def test_get_user():
    user_id = 1  # Assuming a user with this ID exists
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == user_id

def test_update_user():
    user_id = 1  # Assuming a user with this ID exists
    update_data = {
        "nombre": "Updated User",
        "telefono": "0987654321"
    }
    response = client.put(f"/users/{user_id}", json=update_data)
    assert response.status_code == 200
    updated_user = response.json()
    assert updated_user["nombre"] == update_data["nombre"]
    assert updated_user["telefono"] == update_data["telefono"]

def test_delete_user():
    user_id = 1  # Assuming a user with this ID exists
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

def test_create_user_invalid_email():
    user_data = {
        "nombre": "Invalid User",
        "email": "invalidemail",
        "telefono": "1234567890",
        "password": "securepassword"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 422  # Unprocessable Entity for invalid email