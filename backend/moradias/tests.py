# backend/moradias/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MoradiasAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Estamos prevendo que a rota se chamará 'moradia-list'
        self.url = '/api/moradias/' 

    def test_acesso_negado_para_usuario_nao_autenticado(self):
        """TDD: Um usuário sem token não pode ver a lista de moradias"""
        response = self.client.get(self.url)
        # Esperamos 401 Unauthorized ou 403 Forbidden
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_criar_moradia_valida(self):
        """TDD: O endpoint de POST deve aceitar criar uma moradia (Simulando auth por enquanto)"""
        payload = {
            "titulo": "Kitnet perto da faculdade",
            "tipo": "kitnet",
            "valor": 600.00
        }
        response = self.client.post(self.url, payload, format='json')
        # Por enquanto vai falhar com 404, mas quando criarmos a view, queremos 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)