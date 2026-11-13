from fastapi.testclient import TestClient

from main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_coupon_valid():
    with TestClient(app) as client:
        response = client.post(
            "api/coupons",
            json={"name": "Welcome Coupon", "total_quantity": 10},
        )

    assert response.status_code == 200
    assert response.json() == {
        "name": "Welcome Coupon",
        "total_quantity": 10,
    }


def test_create_coupon_zero_quantity():
    with TestClient(app) as client:
        response = client.post(
            "/api/coupons",
            json={"name": "Welcome Coupon", "total_quantity": 0},
        )

    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "total_quantity"]
