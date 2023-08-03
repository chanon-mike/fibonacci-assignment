from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_fib_no_query():
    response = client.get("/fib", headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Query parameter is required"}


def test_fib_decimal_query():
    response = client.get("/fib?n=-1.5", headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Number must be integer"}


def test_fib_string_query():
    response = client.get("/fib?n=xyz", headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert response.json() == {"status": 400, "message": "Number must be integer"}


def test_fib_negative_query():
    response = client.get("/fib?n=-1", headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert response.json() == {
        "status": 400,
        "message": "Number must be equal or greater than 0",
    }


def test_fib_zero_query():
    response = client.get("/fib?n=0", headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"result": 0}


def test_fib_one_query():
    response = client.get("/fib?n=1", headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"result": 1}


def test_fib_two_query():
    response = client.get("/fib?n=2", headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"result": 1}


def test_fib_ten_query():
    response = client.get("/fib?n=10", headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"result": 55}


def test_fib_large_number_query():
    response = client.get("/fib?n=99", headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json() == {"result": 218922995834555169026}
