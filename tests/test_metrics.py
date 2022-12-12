from unittest.mock import Mock, patch


def test_registrations(client):
    with patch("app.routes.metrics_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True

        response = client.post(
            "/metrics/registrations"
        )

    assert response.status_code == 200


def test_logins(client):
    with patch("app.routes.metrics_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True

        response = client.post(
            "/metrics/logins"
        )

    assert response.status_code == 200


def test_registration_counts(client):
    with patch("app.routes.metrics_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True

        response = client.get(
            "/metrics/registrations"
        )

    assert response.status_code == 200
    assert response.text == "0"


def test_login_counts(client):
    with patch("app.routes.metrics_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True

        response = client.get(
            "/metrics/logins"
        )

    assert response.status_code == 200
    assert response.text == "0"


def test_blocked_users(client):
    with patch("app.routes.metrics_routes.requests.get") as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = {"blocked": 0}

        response = client.get(
            "/metrics/blocked_users"
        )

    assert response.status_code == 200
    assert response.json()["blocked"] == 0
