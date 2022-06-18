from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello! Welcome to Shop."

# Testing Unit Drink


def test_add_drink():
    response = client.post("/drink/",
                           json={
                               "name": "Extra Jos Susu",
                               "description": "redbull warkop version",
                               "price": 10000,
                               "category": 1,
                               "type": 1,
                               "size": 1
                           }
                           )
    assert response.status_code == 201
    assert response.json() == [
        {
            "message": "Berhasil dibuat!"
        }
    ]


def test_read_drink():
    response = client.get("/drink/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "description": "redbull warkop version",
            "category": "coffee",
            "id": 1,
            "size": "small",
            "time_updated": "2022-06-17T17:29:16",
            "name": "Extra Jos Susu",
            "price": 10000,
            "type": "hot",
            "time_created": "2022-06-17T17:29:16"
        }
    ]


def test_read_id_drik():
    response = client.get("/drink/1/")
    assert response.status_code == 200
    assert response.json() == {
        "description": "redbull warkop version",
        "id": 1,
        "category": "coffee",
        "size": "small",
        "time_updated": "2022-06-17T17:29:16",
        "name": "Extra Jos Susu",
        "price": 10000,
        "type": "hot",
        "time_created": "2022-06-17T17:29:16"
    }


def test_update_drink():
    response = client.put("drink/1/",
                          json={
                              "name": "Extra Jos Susu",
                              "description": "redbull warkop version",
                              "price": 10000,
                              "category": 1,
                              "type": 1,
                              "size": 1
                          }
                          )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Berhasil dibuat!"
    }


def test_delete_drink():
    response = client.delete("drink/1/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Berhasil dihapus!"
    }
