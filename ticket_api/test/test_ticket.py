from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_animal(self):
        for _ in range(20):
            response = self.client.get(url_for('get_animal'))
            self.assertIn(response.data.decode("utf-8"),["cow", "horse", "duck"])
        # with patch('random.choice') as r:
        #     r.return_value = 'cow'
        #     response = self.client.get(url_for('get_animal'))
        #     self.assertEqual(response.status_code, 200)
        #     self.assertEqual(b'cow', response.data)
        
    def test_get_noise(self):
        test_cases = [("cow","moo"),("horse","neigh"),("duck","quack")]
        for case in test_cases:
            response = self.client.post(url_for('get_noise'), data=case[0])
            self.assertEqual(response.data.decode("utf-8"), case[1])