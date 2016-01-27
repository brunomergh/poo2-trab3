import unittest
import os
from ifes.cdp.pessoa import Pessoa

class TestGeral(unittest.TestCase):


    def test_fabrica(self):
        pessoa = Pessoa()
        self.assertEqual(pessoa.nome, '' )
        self.assertEqual(pessoa.tel, '' )
        self.assertEqual(pessoa.end, '' )
        self.assertEqual(pessoa.tipo, '' )
        self.assertEqual(pessoa.cpf_cnpj, '' )

    def test_apagar(self):

        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteApagar.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Fornecedor;quantia a pagar\n0;3.81\n1;2.4\n2;1.68\n")

    def test_estoque(self):
        FILENAME = os.path.expanduser("~/Desktop/poo2-trab1-master/POO2_Trab1_GabrielaBreder_BrunoMergh/ifes/arquivos/WriteEstoque.txt")
        arqc = open(FILENAME, 'r')
        conteudo = arqc.read()
        self.assertEqual(conteudo, "Codigo;Descricao;Quantidade Atual; \n0;leite;4;\n1;pao doce;5;\n2;pao de sal;6;\n3;po de cafe;3;\n4;miojo;5;\n")



if __name__ == "__main__":
    unittest.main()
