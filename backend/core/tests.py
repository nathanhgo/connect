from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class PingPongAPITest(TestCase):
    def setUp(self):
        # O Django cria um banco de dados temporário limpo para cada teste
        self.client = APIClient()
        self.url = reverse('ping_pong') # Usa o "name" que demos lá no urls.py

    def test_ping_pong_retorna_status_200(self):
        # Ação: Faz uma requisição GET no endpoint
        response = self.client.get(self.url)
        
        # Validação: O status code deve ser 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_ping_pong_retorna_mensagem_correta(self):
        # Ação
        response = self.client.get(self.url)
        
        # Validação: O JSON retornado deve conter a chave "status" com valor "Genial!"
        self.assertEqual(response.json()['status'], 'Genial!')


class UsuarioCustomizadoTest(TestCase):
    
    def test_cria_usuario_com_email_institucional_valido(self):
        """TDD: Deve permitir a criação de usuário com e-mail @aluno.ifsp.edu.br"""
        User = get_user_model()
        user = User.objects.create_user(
            email='nathan@aluno.ifsp.edu.br', 
            password='senhasegura123'
        )
        self.assertEqual(user.email, 'nathan@aluno.ifsp.edu.br')
        self.assertTrue(user.is_active)

    def test_rejeita_usuario_com_email_generico(self):
        """TDD: Deve levantar erro se o e-mail não for institucional"""
        User = get_user_model()
        
        # O 'with self.assertRaises' verifica se o código abaixo gera o erro esperado
        with self.assertRaises(ValidationError):
            user = User(email='nathan@gmail.com', password='senhasegura123')
            user.full_clean() # Força a validação do modelo antes de salvar no banco