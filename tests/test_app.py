from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_meu_ola():
    client = TestClient(app)

    response = client.get("/olar")

    assert response.status_code == HTTPStatus.OK
    assert response.text == "<h1>Olá Meu Mundo</h1>"
