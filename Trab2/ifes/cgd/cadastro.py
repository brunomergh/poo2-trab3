import os
from ifes.util.FabricaGeral import FabricaGeral
from ifes.cgd.daocliente import DAOCliente
from ifes.cgd.daoproduto import DAOProduto
from ifes.cgd.daocompra import DAOCompra
from ifes.cgd.daovenda import DAOVenda
from ifes.cgd.daofornecedor import DAOFornecedor
from ifes.cgd.facade import Facade


class Cadastro:

    @staticmethod
    def popular_banco_cliente():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "cliente.txt")
        arqc = open(path, 'r')
        conteudo = arqc.readline()
        while conteudo != "":

            dadosconteudo = conteudo.split(";")
            p = FabricaGeral.criar('pessoa')
            d = DAOCliente()
            p.nome = dadosconteudo[0]
            p.tel = int(dadosconteudo[1])
            p.end = dadosconteudo[2]
            p.tipo = dadosconteudo[3]
            p.cpf_cnpj = dadosconteudo[4]
            d.insere_cliente(p)
            conteudo = arqc.readline()

    @staticmethod
    def popular_banco_produto():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "produto.txt")
        arqp = open(path, 'r')
        conteudo = arqp.readline()
        while conteudo != "":
            dadosconteudo = conteudo.split(';')
            p = FabricaGeral.criar('produto')
            d = DAOProduto()
            p.desc = dadosconteudo[0]
            p.estmin = int(dadosconteudo[1])
            p.qtdatual = int(dadosconteudo[2])
            p.custo = float(dadosconteudo[3])
            p.pctlucro = float(dadosconteudo[4])
            d.insere_produto(p)
            conteudo = arqp.readline()

    @staticmethod
    def popular_banco_fornecedor():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "fornecedor.txt")
        arqf = open(path, 'r')
        conteudo = arqf.readline()
        while conteudo != "":
            dadosconteudo = conteudo.split(';')
            f = FabricaGeral.criar('fornecedor')
            f.nome = dadosconteudo[0]
            f.end = dadosconteudo[1]
            f.tel = int(dadosconteudo[2])
            f.cnpj = dadosconteudo[3]
            d = DAOFornecedor()
            d.insere_fornecedor(f)
            conteudo = arqf.readline()


    @staticmethod
    def popular_banco_venda():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "venda.txt")
        arqv = open(path, 'r')
        conteudo = arqv.readline()
        while conteudo != "":
            dadosconteudo = conteudo.split(';')
            v = FabricaGeral.criar('venda')
            v.cliente = int(dadosconteudo[0])
            v.dt = dadosconteudo[1]
            v.prod = int(dadosconteudo[2])
            v.qtd = int(dadosconteudo[3])
            d = DAOVenda()
            d.insere_venda(v)
            conteudo = arqv.readline()

    @staticmethod
    def popular_banco_compra():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "compra.txt")
        arqc = open(path, 'r')
        conteudo = arqc.readline()
        while conteudo != "":
            dadosconteudo = conteudo.split(';')
            c = FabricaGeral.criar('compra')
            c.qtd = int(dadosconteudo[0])
            c.notafiscal = dadosconteudo[1]
            c.codfornec = int(dadosconteudo[2])
            c.codprod = int(dadosconteudo[3])
            c.dtcompra = dadosconteudo[4]
            d = DAOCompra()
            d.insere_compra(c)
            conteudo = arqc.readline()

    @staticmethod
    def cadastra_pessoa(dados):

        nome,tel,end,tipo,cpf_cnpj = 0,1,2,3,4
        f, d = Facade.criar('pessoa')
        f.nome = dados[nome]
        f.tel = dados[tel]
        f.end = dados[end]
        f.tipo = dados[tipo]
        f.cpf_cnpj = dados[cpf_cnpj]
        try:
            d.insere_cliente(f)
        except Exception as e:
            raise "Erro ao inserir"

    @staticmethod
    def cadastra_produto(dados):
        p, d = Facade.criar('produto')
        p.desc = dados[0]
        p.estmin = dados[1]
        p.qtdatual = dados[2]
        p.custo = dados[3]
        p.pctlucro = dados[4]

        d.insere_produto(p)

    @staticmethod
    def cadastra_fornecedor(dados):
        f, d = Facade.criar('fornecedor')
        f.nome = dados[0]
        f.end = dados[1]
        f.tel = dados[2]
        f.cnpj = dados[3]
        d.insere_fornecedor(f)

    @staticmethod
    def cadastra_venda(dados):
        v, d = Facade.criar('venda')
        v.cliente = dados[0]
        v.dt = dados[1]
        v.prod = dados[2]
        v.qtd = dados[3]

        d.insere_venda(v)

    @staticmethod
    def cadastra_compra(dados):
        c, d = Facade.criar('compra')

        c.qtd = dados[0]
        c.notaf = dados[1]
        c.codfornec = dados[2]
        c.codprod = dados[3]
        c.dtcompra = dados[4]
        d.insere_compra(c)

    @staticmethod
    def cadastra_login(dados):
        l, d = Facade.criar('login')

        l.login = dados[0]
        l.senha = dados[1]
        tem = False

        for login in d.get_lista_login():
            if login[0] == dados[0]:
                tem = True

        if tem == False:
            d.insere_login(l)