from ifes.cgd.cadastro import Cadastro
from ifes.cgd.relatorio import Relatorio

class Control:
    def __init__(self):
        self.cad = Cadastro()
        self.relatorio = Relatorio()

    def cad_cliente(self,lst):
        try:
            self.cad.cadastra_pessoa(lst)
        except Exception as e:
            raise "Erro ao inserir"
    def cad_login(self,lst):
        self.cad.cadastra_login(lst)

    def cad_fornecedor(self,lst):

        self.cad.cadastra_fornecedor(lst)

    def cad_produto(self,lst):

        self.cad.cadastra_produto(lst)

    def cad_venda(self,lst):
        self.cad.cadastra_venda(lst)

    def cad_compra(self,lst):
        self.cad.cadastra_compra(lst)

    def gerar_relatorio_apagar(self):
        self.relatorio.apagar()

    def gerar_relatorio_areceber(self):
        self.relatorio.areceber()

    def gerar_relatorio_estoque(self):
        self.relatorio.estoque()

    def gerar_relatorio_vendas(self):
         self.relatorio.vendasprod()

    def upload(self):
        self.cad.popular_banco_cliente()
        self.cad.popular_banco_fornecedor()
        self.cad.popular_banco_produto()
        self.cad.popular_banco_compra()
        self.cad.popular_banco_venda()

__author__ = 'Bruno'
