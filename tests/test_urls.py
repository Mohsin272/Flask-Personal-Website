from flask import request


def test_up(client):
    """Test to see if the server is up and running"""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_personal(client):
    resp = client.get("/personal")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_cv(client):
    resp = client.get("/cv")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_comptech(client):
    resp = client.get("/comptech")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_python(client):
    resp = client.get("/comptech/python")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_vsc(client):
    resp = client.get("/comptech/vsc")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_java(client):
    resp = client.get("/comptech/java")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_interests(client):
    resp = client.get("/interests")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_cricket(client):
    resp = client.get("/interests/cricket")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_f1(client):
    resp = client.get("/interests/f1")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_form(client):
    resp = client.get("/form")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)


def test_display(client):
    resp = client.get("/display")
    assert resp.status_code == 200
    assert "<!doctype html>" in resp.get_data(True)
    assert "<thead>" and "</thead>" in resp.get_data(True)


def test_form_operation(client, clean_up_db):
    form_data = {
        "email": "test@test.com",
        "message": "test",
    }
    response = client.post("/processform", data=form_data)
    assert request.method == "POST"
    assert response.status_code == 200
    # resp = response.data  # binary text version of html response
    assert "<!doctype html>" in response.get_data(True)
