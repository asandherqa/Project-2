from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_ticket(self):
        response = self.client.get(url_for('get_ticket'))
        test_ticket = int(response.data.decode("utf-8"))
        expected_range = range(1,100001)
        self.assertIn(test_ticket, expected_range)