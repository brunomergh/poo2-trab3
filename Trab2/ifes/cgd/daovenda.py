__author__ = 'Bruno'

import sqlite3

class DAOVenda():

    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):

        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        data TEXT,
        produto_id INTEGER,
        quantidade INTEGER,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        FOREIGN KEY (produto_id) REFERENCES produtos(id)
        );""")


        self.conn.close()

    def insere_venda(self, v):

        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO VENDAS (cliente_id, data, produto_id, quantidade) VALUES (?,?,?,?)""",  (v.cliente, v.dt, v.prod, v.qtd))
        self.conn.commit()


    def get_vendas(self):
        vendas = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT * FROM vendas ORDER BY cliente_id DESC """)
        for linha in cursor.fetchall():

            vendas.append(linha)

    def delete_venda(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM vendas
        WHERE id = ?
        """, lista)
        self.conn.commit()