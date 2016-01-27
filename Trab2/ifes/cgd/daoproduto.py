__author__ = 'Bruno'

import sqlite3

class DAOProduto():

    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        estoque_minimo INTEGER,
        quantidade_atual INTEGER,
        custo FLOAT,
        percentual_lucro FLOAT
        );""")


        self.conn.close()

    def insere_produto(self, p):

        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO produtos (descricao, estoque_minimo, quantidade_atual, custo, percentual_lucro) VALUES (?,?,?,?,?)""",  (p.desc, p.estmin,p.qtdatual, p.custo, p.pctlucro))
        self.conn.commit()


    def get_produtos(self):
        produtos = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT Nome FROM produtos ORDER BY descricao DESC """)
        for linha in cursor.fetchall():

            produtos.append(linha)

    def update_produto(self,qtdatual, id):
        cursor = self.conn.cursor()
        cursor.execute(""" UPDATE produtos SET quantidade_atual = ? WHERE id = ? """, (qtdatual, id))

    def delete_produto(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM produtos
        WHERE id = ?
        """, lista)
        self.conn.commit()