"""Tests for main application endpoints."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI Enterprise Template"}


def test_health_endpoint(client: TestClient) -> None:
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data
    assert "environment" in data


def test_api_health_endpoint(client: TestClient) -> None:
    """Test the API health check endpoint."""
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data
    assert "environment" in data


def test_api_detailed_health_endpoint(client: TestClient) -> None:
    """Test the detailed API health check endpoint."""
    response = client.get("/api/v1/health/detailed")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data
    assert "environment" in data
    assert "app_name" in data
    assert "debug" in data
    assert "database_url" in data
    assert "cors_enabled" in data
    assert "redis_configured" in data


def test_users_endpoint(client: TestClient) -> None:
    """Test the users endpoint."""
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "email" in data[0]
    assert "full_name" in data[0]
    assert "is_active" in data[0]


def test_user_detail_endpoint(client: TestClient) -> None:
    """Test the user detail endpoint."""
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
    assert "full_name" in data
    assert "is_active" in data


def test_user_detail_not_found(client: TestClient) -> None:
    """Test the user detail endpoint with non-existent user."""
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_create_user_endpoint(client: TestClient) -> None:
    """Test the create user endpoint."""
    user_data = {
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123",
        "is_active": True,
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["full_name"] == user_data["full_name"]
    assert data["is_active"] == user_data["is_active"]
    assert "id" in data
