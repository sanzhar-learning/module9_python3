from fastapi.testclient import TestClient
from task import app

client = TestClient(app)


def test_create_book():
    resp = client.post("/books", json={"title": "Test", "description": "A test book"})
    assert resp.status_code == 200


def test_list_books():
    resp = client.get("/books")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_book():
    resp = client.get("/books/1")
    assert resp.status_code == 200


test_create_book()
test_list_books()
test_get_book()
