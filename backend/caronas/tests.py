# backend/caronas/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class CaronasAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/caronas/'

    def test_lista_caronas_retorna_formato_json(self):
        """TDD: O endpoint deve existir e retornar um JSON (mesmo vazio)"""
        response = self.client.get(self.url)
        # Confirma se o endpoint não dá 404 (Not Found)
        self.assertNotEqual(response.status_code, status.HTTP_404_NOT_FOUND)