from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_hello() -> None:
    r = client.get("/hello", params={"name": "tima"})
    assert r.json() == {"message": "hello, tima"}
