from unittest.mock import Mock, patch


def test_signup_admin_ok(client):
    admin = {
        "email": "test_email@gmail.com",
        "username": "test_username",
        "password": "test_pass",
        "surname": "test_surname",
    }

    response = client.post(
        "/admins/signup",
        json=admin,
    )

    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == admin["email"]
    assert data["username"] == admin["username"]
    assert data["surname"] == admin["surname"]


def test_signup_admin_without_email(client):

    admin = {
        "username": "test_username",
        "password": "test_pass",
        "surname": "test_surname",
    }

    response = client.post(
        "/admins/signup",
        json=admin,
    )

    assert response.status_code == 422, response.text


def test_signup_same_admin_twice(client):
    admin = {
        "email": "test_email@gmail.com",
        "username": "test_username",
        "password": "test_pass",
        "surname": "test_surname",
    }

    response1 = client.post(
        "/admins/signup",
        json=admin,
    )

    response2 = client.post(
        "/admins/signup",
        json=admin,
    )

    assert response1.status_code == 201
    assert response2.status_code == 409
    assert response2.json()["detail"] == "The user already exists"
