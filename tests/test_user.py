from tests.config import client, test_user, test_admin, test_db, setup_test_db


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API!"}


def test_create_user_token(test_user):
    response = client.post(
        "/token", data={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_read_user_route(test_user):
    token_response = client.post(
        "/token", data={"username": "testuser", "password": "testpassword"}
    )
    token = token_response.json().get("access_token")
    assert token is not None
    response = client.get("/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo, usuário!"}


def test_read_admin_route(test_admin):
    token_response = client.post(
        "/token", data={"username": "testadmin", "password": "adminpassword"}
    )
    token = token_response.json().get("access_token")
    assert token is not None
    response = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo, administrador!"}


def test_user_cannot_access_admin_route(test_user):
    token_response = client.post(
        "/token", data={"username": "testuser", "password": "testpassword"}
    )
    token = token_response.json().get("access_token")
    assert token is not None
    response = client.get("/admin", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 403
    assert response.json() == {"detail": "Acesso não autorizado"}


def test_invalid_token():
    response = client.get("/user", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Could not validate credentials"}
