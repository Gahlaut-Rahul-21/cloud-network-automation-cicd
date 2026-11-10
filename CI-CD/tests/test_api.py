import pytest

from app.main import create_app


@pytest.fixture()
def client():
    return create_app().test_client()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_subnet_ok(client):
    resp = client.get("/subnet", query_string={"cidr": "192.168.1.0/24"})
    assert resp.status_code == 200
    assert resp.get_json()["usable_hosts"] == 254


def test_subnet_bad_input(client):
    assert client.get("/subnet", query_string={"cidr": "bogus"}).status_code == 400


def test_overlap(client):
    resp = client.get("/overlap", query_string={"a": "10.0.0.0/16", "b": "10.0.5.0/24"})
    assert resp.get_json()["overlap"] is True


def test_split(client):
    resp = client.get("/split", query_string={"cidr": "10.0.0.0/24", "prefix": 25})
    assert resp.get_json()["subnets"] == ["10.0.0.0/25", "10.0.0.128/25"]


def test_split_bad_prefix(client):
    resp = client.get("/split", query_string={"cidr": "10.0.0.0/24", "prefix": "x"})
    assert resp.status_code == 400
