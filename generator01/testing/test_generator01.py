from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase
from random import randint

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def rand_country(self):

        countries = ['German', 'Spanish', 'French', 'Russian', 'Chinese', 'Portuguese','Hindi','Arabic','Japanese', 'Korean'] 
        response = self.client.get(url_for("random_generator"))
        self.assertIn(countries[int(response.data)-1], countries)

    def test_country(self):
        with patch("requests.get") as g:
            g.return_value.text = b"1"
            response = self.client.get(url_for("random_generator"))
            random_output = ['1','2','3','4','5','6','7','8','9','10']
            self.assertIn(response.data.decode('utf-8'), random_output)
