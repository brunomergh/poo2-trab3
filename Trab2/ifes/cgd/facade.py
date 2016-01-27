__author__ = 'Bruno'

from ifes.util.FabricaGeral import FabricaGeral
from ifes.cgd.daocliente import DAOCliente
from ifes.cgd.daofornecedor import DAOFornecedor
from ifes.cgd.daoproduto import DAOProduto
from ifes.cgd.daocompra import DAOCompra
from ifes.cgd.daovenda import DAOVenda
from ifes.cgd.daologin import DAOLogin

class Facade():

    def criar(nome):

        dados = {}
        dados['pessoa'] = DAOCliente()
        dados['fornecedor'] = DAOFornecedor()
        dados['produto'] = DAOProduto()
        dados['compra'] = DAOCompra()
        dados['venda'] = DAOVenda()
        dados['login'] = DAOLogin()

        f = FabricaGeral.criar(nome)
        d = dados[nome]

        return f,d
