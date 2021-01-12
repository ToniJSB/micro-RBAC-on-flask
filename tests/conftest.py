import os
import tempfile

import pytest
from app_flask.app import create_app
from app_flask.app.database import db

with open(os.path.join(os.path.dirname(__file__), 'modelodb.sql'), 'rb') as f:
    _data_sql = f.read().decode(encoding='ISO-8859-1')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    ejec = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with ejec.app_context():
        db.create_all(app=ejec)

    yield ejec

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='Admin', password='Admin'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)