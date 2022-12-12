from unittest.mock import Mock, patch


def test_users_list(client):
    with patch("app.routes.users_admin_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = []

        response = client.get(
            "/users/"
        )

    assert response.status_code == 200
    assert response.json() == []


def test_passengers_info_ok(client):
    with patch("app.routes.users_admin_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {
            "email": "test_user@gmail.com",
            "username": "test_username",
            "surname": "test_surname",
            "ratings": 5
        }

        response = client.get(
            "/users/passengers/test_user@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["email"] == "test_user@gmail.com"
    assert response.json()["username"] == "test_username"


def test_drivers_info_ok(client):
    with patch("app.routes.users_admin_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {
            "email": "test_user@gmail.com",
            "username": "test_username",
            "surname": "test_surname",
            "ratings": 5,
            "licence_plate": "test_licence_plate",
            "model": "test_model"
        }

        response = client.get(
            "/users/drivers/test_user@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["email"] == "test_user@gmail.com"
    assert response.json()["username"] == "test_username"
    assert response.json()["licence_plate"] == "test_licence_plate"


def test_user_blocked(client):
    with patch("app.routes.users_admin_routes.requests.post") as mock_post:
        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = {"message": "User blocked"}

        response = client.post(
            "/users/blocked/test_user@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["message"] == "User blocked"


def test_user_unblocked(client):
    with patch("app.routes.users_admin_routes.requests.post") as mock_post:
        mock_post.return_value.ok = True
        mock_post.return_value.json.return_value = {"message": "User unblocked"}

        response = client.post(
            "/users/unblocked/test_user@gmail.com"
        )

    assert response.status_code == 200
    assert response.json()["message"] == "User unblocked"



