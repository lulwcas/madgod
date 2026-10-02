from app import app

def test_result():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"mad god" in response.data