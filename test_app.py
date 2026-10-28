from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Iris Flower Classifier" in response.data


def test_prediction():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "sepal_length": "5.1",
            "sepal_width": "3.5",
            "petal_length": "1.4",
            "petal_width": "0.2"
        }
    )

    assert response.status_code == 200
    assert b"Predicted species:" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_invalid_input():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "sepal_length": "abc",
            "sepal_width": "3.5",
            "petal_length": "1.4",
            "petal_width": "0.2"
        }
    )

    assert response.status_code == 200
    assert b"Please enter four valid numeric measurements" in response.data