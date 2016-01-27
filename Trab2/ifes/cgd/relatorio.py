import os
import sqlite3
from ifes.cgd.daoproduto import DAOProduto
from datetime import datetime
import locale

class Relatorio:

    @staticmethod
    def apagar():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteApagar.txt")
        arquivo = open(path, 'w')
        arquivo.write("Fornecedor | quantia a pagar\n")
        total = 0

        conn = sqlite3.connect('padoca.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT fornecedores.id, sum(produtos.custo*compras.quantidade)
        FROM fornecedores
        INNER JOIN compras ON (fornecedores.id = compras.codigo_fornecedor)
        INNER JOIN produtos ON (compras.codigo_produto = produtos.id)
        GROUP BY fornecedores.id""")

        iterator = iter(cursor.fetchall())
        try:
            while True:
                linha = next(iterator)
                arquivo.write(str(linha[0]) + "          | " + str(linha[1]) + "\n")
        except StopIteration:
            pass



    @staticmethod
    def areceber():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteAreceber.txt")
        arquivo = open(path, 'w')
        arquivo.write("Cliente | quantia a receber\n")

        conn = sqlite3.connect('padoca.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT clientes.id, round(sum((((produtos.percentual_lucro/100)*produtos.custo) + produtos.custo) * vendas.quantidade),2)
        FROM clientes
        INNER JOIN vendas ON (clientes.id = vendas.cliente_id)
        INNER JOIN produtos ON (vendas.produto_id = produtos.id)
        GROUP BY clientes.id""")

        now = datetime.now()

        iterator = iter(cursor.fetchall())
        try:
            while True:
                linha = next(iterator)
                if now.day == 25:
                    arquivo.write(str(linha[0]) + "       | " + str(linha[1] - linha[1]*5/100) + "\n")
                else:
                    arquivo.write(str(linha[0]) + "       | " + str(linha[1]) + "\n")
        except StopIteration:
            pass



    @staticmethod
    def vendasprod():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteVendasPorProd.txt")
        arquivo = open(path, 'w')
        arquivo.write("Descricao do Produto | Total de venda bruta | Total de lucro\n")


        conn = sqlite3.connect('padoca.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT produtos.id, round(sum((((produtos.percentual_lucro/100)*produtos.custo) + produtos.custo) * vendas.quantidade),2), round(sum(((produtos.percentual_lucro/100)*produtos.custo) * vendas.quantidade),2)
        FROM produtos
        INNER JOIN vendas ON (produtos.id = vendas.produto_id)
        GROUP BY produtos.id""")

        iterator = iter(cursor.fetchall())
        try:
            while True:
                linha = next(iterator)
                arquivo.write(str(linha[0]) + "                    | " + str(linha[1]) + "                  | " + str(linha[2]) +"\n")
        except StopIteration:
            pass



    @staticmethod
    def estoque():

        file = os.path.split(os.path.abspath(__file__))[0]
        diretorio = file.replace("cgd", "")
        path = os.path.join(diretorio, 'arquivos/', "WriteEstoque.txt")
        arquivo = open(path, 'w')
        d = DAOProduto()
        conn = sqlite3.connect('padoca.db')
        cursor = conn.cursor()
        cursor2 = conn.cursor()

        cursor.execute("""SELECT (produtos.quantidade_atual + compras.quantidade)
        FROM produtos
        INNER JOIN compras ON (produtos.id = compras.codigo_produto)
        GROUP BY produtos.id""")
        lst1 = []
        for linha in cursor.fetchall():
            lst1.append(linha[0])

        cursor2.execute("""SELECT sum(vendas.quantidade)
        FROM produtos
        INNER JOIN vendas ON (produtos.id = vendas.produto_id)
        GROUP BY produtos.id""")
        lst = []
        for linha in cursor2.fetchall():
            lst.append(linha[0])

        for i in range(len(lst1)):
            d.update_produto(lst1[i] - lst[i],i+1)

        arquivo.write("Codigo | Quantidade Atual \n")

        cursor.execute("""SELECT produtos.estoque_minimo
         FROM produtos""")
        lstqtdatual = []
        for linha in cursor.fetchall():
            lstqtdatual.append(linha[0])

        for i in range(len(lst1)):
            if ((lst1[i] - lst[i]) <= lstqtdatual[i]):
                arquivo.write(str(i+1) + "      | " + str(lst1[i] - lst[i]) + " <============== COMPRAR MAIS \n")
            else:
                arquivo.write(str(i+1) + "      | " + str(lst1[i] - lst[i]) + "\n")
