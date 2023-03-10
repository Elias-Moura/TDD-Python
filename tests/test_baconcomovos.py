"""TDD - Test driven development (Desenvolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar o código
"""
import unittest
from baconcomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertionerror_se_nao_receber_int_ou_float(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('2')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrata_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"'
                )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_a_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 4, 7, 8, 2.2, 11)
        saida = 'Passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"')

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_apenas_3(self):
        entradas = (3, 6, 9, 12, 21)
        saida = 'Bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"')

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_apenas_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'Ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada),
                                 saida,
                                 msg=f'"{entrada}" não retornou "{saida}"')

