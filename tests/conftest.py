# flake8: noqa: E402
import sys
import os

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
