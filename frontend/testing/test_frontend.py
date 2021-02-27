from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_frontend(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"

            response = self.client.get(url_for("home"))
            self.assertIn(b'1', response.data)
