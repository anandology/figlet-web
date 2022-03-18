import pytest
import sys
import flask
sys.path.append(".")

from webapp import app as _app

@pytest.fixture()
def app():
    _app.config.update({
        "TESTING": True,
    })
    yield _app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200

HELLO = r"""
 _          _ _
| |__   ___| | | ___
| '_ \ / _ \ | |/ _ \
| | | |  __/ | | (_) |
|_| |_|\___|_|_|\___/
"""

def has_lines_in_text(text, html):
    return all(line in html for line in text.splitlines())

def test_hello(client):
    response = client.get("/?text=hello")
    assert response.status_code == 200

    hello = str(flask.escape(HELLO.strip("\n")))
    html = response.get_data(as_text=True)
    assert has_lines_in_text(hello, html)

