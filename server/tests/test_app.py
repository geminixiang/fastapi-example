from fastapi.testclient import TestClient
from pytest import mark
from app import app

client = TestClient(app)

@mark.user
def test_get_user():
    response = client.get(
        "/v1/user?v=alyce91",
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": "63afcc2e6e4a470112df9f54",
        "email": "alyce_colon@geekola.foo",
        "username": "alyce91",
        "profile": {
        "name": "Alyce Colon",
        "company": "Geekola",
        "dob": "1991-09-05",
        "address": "96 Monroe Street, Mammoth, Virgin Islands",
        "location": {
            "lat": 10.270219,
            "long": -23.214673
        },
        "about": "Ut tempor occaecat irure irure ea aliqua. Do nisi magna quis et officia non fugiat amet."
        },
        "apiKey": "f4b73afb-3a45-4e40-a6b2-864d448717f6",
        "roles": [
        "owner",
        "member"
        ],
        "createdAt": "2013-06-04T17:18:03.073Z",
        "updatedAt": "2013-06-05T17:18:03.073Z"
    }

@mark.user
def test_failed_get_user():
    response = client.get(
        "/v1/user?v=alyce911",
    )

    assert response.status_code == 400
    assert response.text == "not exists"

@mark.user
def test_post_user():
    response = client.post(
        "/v1/user?v=alyce91", 
        json={"email": "qooji3k27@geekola.foo"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "id": "63afcc2e6e4a470112df9f54",
        "email": "qooji3k27@geekola.foo",
        "username": "alyce91",
        "profile": {
        "name": "Alyce Colon",
        "company": "Geekola",
        "dob": "1991-09-05",
        "address": "96 Monroe Street, Mammoth, Virgin Islands",
        "location": {
            "lat": 10.270219,
            "long": -23.214673
        },
        "about": "Ut tempor occaecat irure irure ea aliqua. Do nisi magna quis et officia non fugiat amet."
        },
        "apiKey": "f4b73afb-3a45-4e40-a6b2-864d448717f6",
        "roles": [
        "owner",
        "member"
        ],
        "createdAt": "2013-06-04T17:18:03.073Z",
        "updatedAt": "2013-06-05T17:18:03.073Z"
    }

@mark.user
def test_failed_post_user():
    response = client.post(
        "/v1/user?v=alyce911",
        json={"email": "qooji3k27@geekola.foo"}
    )

    assert response.status_code == 400
    assert response.text == "not exists"
