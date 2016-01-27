__author__ = 'Bruno'

import sqlite3

class DAOCompra():

    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):

        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS compras (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        quantidade INTEGER NOT NULL,
        nota_fiscal TEXT,
        codigo_fornecedor INTEGER,
        codigo_produto INTEGER,
        data TEXT,
        FOREIGN KEY(codigo_fornecedor) REFERENCES fornecedores(id)
        FOREIGN KEY(codigo_produto) REFERENCES produtos(id)
        );""")


        self.conn.close()

    def insere_compra(self, c):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO compras (quantidade, nota_fiscal, codigo_fornecedor, codigo_produto, data) VALUES (?,?,?,?,?)""", (c.qtd, c.notafiscal, c.codfornec, c.codprod, c.dtcompra))
        self.conn.commit()


    def get_compras(self):
        compras = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT * FROM produtos ORDER BY codigo_fornecedor DESC """)
        for linha in cursor.fetchall():

            compras.append(linha)

    def delete_compra(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM produtos
        WHERE id = ?
        """, lista)
        self.conn.commit()