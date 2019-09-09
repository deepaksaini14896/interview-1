from starlette.testclient import TestClient

from sql_app.main import app

client = TestClient(app)


def test_read_location():
    response = client.get("/get_location/28.6333&77.2167")
    assert response.status_code == 200
    assert response.json() == {
        "pincode": "IN/110001",
        "address": "Connaught Place",
        "city": "New Delhi",
    }


def test_read_location_existing_data():
    response = client.get("/get_location/28.6333&77.2168")
    assert response.status_code == 404
    assert response.json() == {"detail": "Latitude and Longitude are not exist."}


def test_create_location():
    response = client.post("/post_location/IN250002&phool&meerut&14.0001&12.0001")
    assert response.status_code == 200
    assert response.json() == {"pincode": "IN250002"}


def test_create_existing_data():
    response = client.post("/post_location/IN250002&phool&meerut&14.0001&12.0001")
    assert response.status_code == 400
    assert response.json() == {"detail": "Don't assume that they will exactly be the same."}