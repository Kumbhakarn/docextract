import pytest
from fastapi.testclient import TestClient

from docextract.app import create_app


@pytest.fixture
def client() -> TestClient:
    return TestClient(create_app())


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "ok"}


def test_health_rejects_other_methods(client: TestClient) -> None:
    response = client.post("/health")

    assert response.status_code == 405


def test_unknown_route_returns_404(client: TestClient) -> None:
    response = client.get("/does-not-exist")

    assert response.status_code == 404


def test_openapi_documents_health(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()

    assert "/health" in schema["paths"]
    assert "HealthResponse" in schema["components"]["schemas"]
