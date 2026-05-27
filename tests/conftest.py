import pytest
from app import create_app
from app.models import db, Candidate


@pytest.fixture(scope="session")
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    }
    application = create_app(config=test_config)

    with application.app_context():
        db.create_all()
        seed_candidate = Candidate(name="Alice Sharma", email="alice@example.com")
        db.session.add(seed_candidate)
        db.session.commit()

    yield application


@pytest.fixture()
def client(app):
    return app.test_client()
