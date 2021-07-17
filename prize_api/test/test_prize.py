from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_prize_Ferrari(self):
        response = self.client.post(url_for('get_prize'), data='Ferrari')
        self.assertIn(response.data.decode('utf-8'), ['488', 'Roma', '812'])
    def test_get_prize_Lamborghini(self):
        response = self.client.post(url_for('get_prize'), data='Lamborghini')
        self.assertIn(response.data.decode('utf-8'), ['Aventador', 'Huracan', 'Urus'])
    def test_get_prize_McLaren(self):
        response = self.client.post(url_for('get_prize'), data='McLaren')
        self.assertIn(response.data.decode('utf-8'), ['720S', 'Senna', '570S'])
    def test_get_prize_Rolex(self):
        response = self.client.post(url_for('get_prize'), data='Rolex')
        self.assertIn(response.data.decode('utf-8'), ['Day-Date', 'Datejust', 'Sky Dweller'])        
    def test_get_prize_AP(self):
        response = self.client.post(url_for('get_prize'), data='Audemars Piguet')
        self.assertIn(response.data.decode('utf-8'), ['Millenary', 'Royal Oak', 'Code 11.59'])
    def test_get_prize_RM(self):
        response = self.client.post(url_for('get_prize'), data='Richard Mille')
        self.assertIn(response.data.decode('utf-8'), ['74-02', '74-01', '72-01']) 
    def test_get_prize_error(self):
        response = self.client.post(url_for('get_prize'), data='nothing')
        self.assertIn(response.data.decode('utf-8'), ['No model error'])           
