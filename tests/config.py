import pytest
from fastapi.testclient import TestClient

from app.core.database import Base, engine, get_db
from app.core.security import get_password_hash
from app.main import app
from app.models.user import User

client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def test_db(setup_test_db):
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session")
def test_user(test_db):
    user = User(
        username="testuser",
        hashed_password=get_password_hash("testpassword"),
        role="user",
    )
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user


@pytest.fixture(scope="session")
def test_admin(test_db):
    admin = User(
        username="testadmin",
        hashed_password=get_password_hash("adminpassword"),
        role="admin",
    )
    test_db.add(admin)
    test_db.commit()
    test_db.refresh(admin)
    return admin
