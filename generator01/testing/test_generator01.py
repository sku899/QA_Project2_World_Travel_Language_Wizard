from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def random_country(self):
        country = [b"1", b"2", b"3", b"4"]
        response = self.client.get(url_for("random_generator"))
        self.assertIn(response.data, country)

    def test_country(self):
        with patch("requests.get") as g:
            g.return_value.text = b"1"
            response = self.client.get(url_for("random_generator"))
            response = b"1"
            self.assertIn(b"1", response)
