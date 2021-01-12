from app_flask.app import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_permiso_view_no_logged(client):
    response = client.get('/permiso/view')    
    assert response._status_code == 401
def test_rol_view_no_logged(client):
    response = client.get('/rol/view')    
    assert response._status_code == 401
def test_usuario_view_no_logged(client):
    response = client.get('/usuario/view')    
    assert response._status_code == 401

