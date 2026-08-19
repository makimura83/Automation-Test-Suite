import pytest

def test_get_request(api_session):
    response = api_session.get("https://httpbin.org/get")
    assert response.status_code == 200
    assert "headers" in response.json()

def test_status_code_404(api_session):
    response = api_session.get("https://httpbin.org/status/404")
    assert response.status_code == 404