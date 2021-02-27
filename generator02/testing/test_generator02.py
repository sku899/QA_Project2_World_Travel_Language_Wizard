from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def rand_first_translate (self):
        first_translate = ['Willkommen', 'Danke', 'Guten Morgen', 'Wie geht es Ihnen']
        response = self.client.get(url_for("random_generator"))
        self.assertIn(first_translate[int(response.data.decode('utf-8'))-1], first_translate)


    def rand_tenth_translate (self):
        tenth_translate = ['어서 오십시오','감사합니다','좋은 아침', '어떻게 지내']
        response = self.client.get(url_for("random_generator"))
        self.assertIn(tenth_translate[int(response.data.decode('utf-8'))-1], tenth_translate)


    def test_country(self):
        with patch("requests.get") as g:
            g.return_value.text = b"1"
            response = self.client.get(url_for("random_generator"))
            random_output = ['1','2','3','4']
            self.assertIn(response.data.decode('utf-8'), random_output)
