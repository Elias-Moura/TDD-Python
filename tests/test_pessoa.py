from pessoa import Pessoa
import unittest
from unittest.mock import patch

'''
setUp() # Coisa que devem acontecer antes do teste
tearDown() #coisas que devem acontecer depois do teste
'''


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Elias', 'Moura')

    def test_pessoa_attr_nome_e_str(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Elias')

    def test_pessoa_attr_sobrenome_e_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Moura')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos, 'Moura')

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_dados(), 'ERROR 404')
            self.assertFalse(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_e_falha_sequencial(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obter_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obter_dados(), 'ERROR 404')
            self.assertFalse(self.p1.dados_obtidos)


