import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from email_app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_dashboard_page():
    client = app.test_client()
    response = client.get("/dashboard")

    assert response.status_code == 200
