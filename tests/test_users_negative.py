def test_invalid_user_returns_404(api_client):
    response = api_client.get("/users/99999")

    assert response.status_code == 404
    assert response.text is not None

def test_invalid_endpoint_returns_404(api_client):
    response = api_client.get("/invalid-endpoint")

    assert response.status_code == 404


def test_valid_endpoint_does_not_return_server_error(api_client):
    response = api_client.get("/users/1")

    assert response.status_code < 500