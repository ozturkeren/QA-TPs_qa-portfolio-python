import requests
import pytest

@pytest.mark.api
def test_list_users_ok():
    r = requests.get("https://reqres.in/api/users", params={"page": 2}, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "data" in data and len(data["data"]) > 0
