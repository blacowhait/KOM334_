from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello! Welcome to Shop."

# Testing Unit Drink


def test_read_drink():
    response = client.get("/drink/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "description": "A cappuccino is an espresso-based coffee drink that originated in Austria with later development taking place in Italy, and is prepared with steamed milk foam",
            "category": "1",
            "size": "1",
            "time_updated": "2022-06-18T03:36:51",
            "price": 25000,
            "name": "Cappuccino",
            "type": "1",
            "time_created": "2022-06-18T03:36:19"
        },
        {
            "id": 2,
            "description": "A cappuccino is an espresso-based coffee drink that originated in Austria with later development taking place in Italy, and is prepared with steamed milk foam",
            "category": "coffee",
            "size": "small",
            "time_updated": "2022-06-18T06:04:21",
            "price": 25000,
            "name": "Cappuccino",
            "type": "hot",
            "time_created": "2022-06-18T06:04:21"
        },
        {
            "id": 3,
            "description": "Darjeeling tea is a tea made from Camellia sinensis var",
            "category": "tea",
            "size": "small",
            "time_updated": "2022-06-18T03:39:21",
            "price": 23000,
            "name": "Darjeeling tea ",
            "type": "hot",
            "time_created": "2022-06-18T03:39:21"
        },
        {
            "id": 4,
            "description": "Iced tea is a form of cold tea",
            "category": "tea",
            "size": "medium",
            "time_updated": "2022-06-18T03:48:54",
            "price": 23000,
            "name": "Iced tea",
            "type": "cold",
            "time_created": "2022-06-18T03:48:54"
        }
    ]


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
    assert response.json() == {
        "message": "Berhasil dibuat!"
    }


def test_read_id_drik():
    response = client.get("/drink/1/")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "description": "A cappuccino is an espresso-based coffee drink that originated in Austria with later development taking place in Italy, and is prepared with steamed milk foam",
        "category": "1",
        "size": "1",
        "time_updated": "2022-06-18T03:36:51",
        "price": 25000,
        "name": "Cappuccino",
        "type": "1",
        "time_created": "2022-06-18T03:36:19"
    }


def test_update_drink():
    response = client.put("drink/5",
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
        "message": "Berhasil diupdate!"
    }


def test_delete_drink():
    response = client.delete("drink/5")
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Drink with id 5 successfully deleted"
    }

# Testing unit Order


def test_read_order():
    response = client.get("/order/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "time_created": "2022-06-18T05:58:45",
            "status": "pending",
            "buyer_id": 1,
            "total_price": 73000,
            "id": 1,
            "time_updated": "2022-06-18T06:09:38",
            "buyer": {
                "id": 1,
                "email": "akaasyahnurfath@gmail.com",
                "time_created": "2022-06-18T03:34:46",
                "name": "Akaasyah Nurfath",
                "whatsapp": "string",
                "time_updated": "2022-06-18T03:34:46"
            },
            "foods": [
                {
                    "description": "Carbonara is an Italian pasta dish from Rome made with eggs, hard cheese, cured pork, and black pepper",
                    "category": "main_course",
                    "id": 3,
                    "time_updated": "2022-06-18T03:40:57",
                    "name": "Carbonara",
                    "price": 35000,
                    "time_created": "2022-06-18T03:40:57"
                },
                {
                    "description": "Pancake is a flat cake, often thin and round, prepared from a starch-based batter that may contain eggs, milk and butter and cooked on a hot surface such as a griddle or frying pan, often frying with oil or butter",
                    "category": "dessert",
                    "id": 4,
                    "time_updated": "2022-06-18T03:42:00",
                    "name": "Pancake",
                    "price": 15000,
                    "time_created": "2022-06-18T03:42:00"
                }
            ],
            "drinks": [
                {
                    "id": 4,
                    "description": "Iced tea is a form of cold tea",
                    "category": "tea",
                    "size": "medium",
                    "time_updated": "2022-06-18T03:48:54",
                    "price": 23000,
                    "name": "Iced tea",
                    "type": "cold",
                    "time_created": "2022-06-18T03:48:54"
                }
            ]
        }
    ]


def test_read_id_order():
    response = client.get("/order/1/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "pending",
        "time_created": "2022-06-18T05:58:45",
        "buyer_id": 1,
        "total_price": 73000,
        "id": 1,
        "time_updated": "2022-06-18T06:09:38",
        "buyer": {
            "email": "akaasyahnurfath@gmail.com",
            "id": 1,
            "time_created": "2022-06-18T03:34:46",
            "name": "Akaasyah Nurfath",
            "whatsapp": "string",
            "time_updated": "2022-06-18T03:34:46"
        },
        "foods": [
            {
                "category": "main_course",
                "description": "Carbonara is an Italian pasta dish from Rome made with eggs, hard cheese, cured pork, and black pepper",
                "id": 3,
                "time_updated": "2022-06-18T03:40:57",
                "name": "Carbonara",
                "price": 35000,
                "time_created": "2022-06-18T03:40:57"
            },
            {
                "category": "dessert",
                "description": "Pancake is a flat cake, often thin and round, prepared from a starch-based batter that may contain eggs, milk and butter and cooked on a hot surface such as a griddle or frying pan, often frying with oil or butter",
                "id": 4,
                "time_updated": "2022-06-18T03:42:00",
                "name": "Pancake",
                "price": 15000,
                "time_created": "2022-06-18T03:42:00"
            }
        ],
        "drinks": [
            {
                "id": 4,
                "description": "Iced tea is a form of cold tea",
                "category": "tea",
                "size": "medium",
                "time_updated": "2022-06-18T03:48:54",
                "price": 23000,
                "name": "Iced tea",
                "type": "cold",
                "time_created": "2022-06-18T03:48:54"
            }
        ]
    }


def test_error_create_order():
    response = client.post("/order/",
                           json={
                               "total_price": 0,
                               "drinks": [
                                   4
                               ],
                               "foods": [
                                   3, 4
                               ],
                               "buyer_id": 0
                           }
                           )
    assert response.status_code == 500
    assert response.json() == {
        "detail": "Something Happened during creating Order"
    }


def test_create_order():
    response = client.post("/order/",
                           json={
                               "total_price": 73000,
                               "drinks": [
                                   4
                               ],
                               "foods": [
                                   3, 4
                               ],
                               "buyer_id": 1
                           }
                           )
    assert response.status_code == 201
    assert response.json() == {
        "message": "Berhasil dibuat!"
    }


def test_update_status_order():
    response = client.post("order/status/2?request=1")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Status berhasil diupdate!"
    }


def test_delete_order():
    response = client.delete("order/2")
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Order with id 2 successfully deleted"
    }
