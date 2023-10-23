from fastapi.testclient import TestClient
# from ..src.main import app
from src.main import app

client = TestClient(app)

def test_get_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg":"hello_worldAAA"}

def test_get_api_path():
    response = client.get("/books/path")
    assert response.status_code == 200
    assert response.json() == {"msg": "path"}

def test_get_api_qeury():
    response = client.get("/books/?title=MyTitle")
    assert response.status_code == 200
    assert response.json() == {"msg": "MyTitle"}

def test_create_book():
    data = {"title": "New Book Title", "author": "Author Name"}
    response = client.post("/books/create_book", json=data)
    assert response.status_code == 200
    assert response.json() == {"msg": data}

def test_update_book():
    book_id = 1
    data = {"title": "Updated Title", "author": "Updated Author"}
    response = client.put(f"/books/update_book/{book_id}", json=data)
    assert response.status_code == 200
    assert response.json() == {"meg": data}

    book_id = 3
    response = client.put(f"/books/update_book/{book_id}", json=data)
    assert response.status_code == 404