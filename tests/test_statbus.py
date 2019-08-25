

import pytest

from statbus import app


@pytest.fixture
def client():
    # Set testing and create test client
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

    # Cleanup if required


def test_homepage(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data