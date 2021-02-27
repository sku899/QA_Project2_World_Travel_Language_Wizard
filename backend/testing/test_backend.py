from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase
import json

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_translate(self):
        welcome = ['Willkommen', 'Bienvenida, Bienvenido', 'Bienvenue, Bienvenu', \
            'Добро пожаловать', '欢迎', 'Receber','स्वागत हे','أهلا بك']
        for i in range(0,8):
            with patch("requests.get") as g:
                g.return_value.text = '1'
                response = self.client.get(url_for("random_generator_temp"))
                if i==0:
                    self.assertIn(bytes(welcome[i], 'utf-8'), response.data)
                else:
                    self.assertNotIn(bytes(welcome[i], 'utf-8'), response.data)
