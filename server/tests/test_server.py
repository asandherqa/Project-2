from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://pryze_ticket_api:5000/get_ticket', text = '39403')
            mocker.post('http://pryze_class_api:5000/get_class', text = 'Porsche')
            mocker.post('http://pryze_prize_api:5000/get_prize', text = '911')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'A Porsche 911, Good luck!', response.data)
