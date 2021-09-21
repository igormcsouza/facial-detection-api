from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_read_main():
    with open("tests/files/img_base64.txt") as p:
        img_64 = p.readline()

    response = client.post("/detect",
                           json={"img": img_64})
    assert response.status_code == 200
