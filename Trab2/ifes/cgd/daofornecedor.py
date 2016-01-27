__author__ = 'Bruno'

import sqlite3

class DAOFornecedor():

    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT,
        fone TEXT,
        Cnpj INT
        );""")



    def insere_fornecedor(self, f):

        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO fornecedores (nome, endereco, fone, Cnpj) VALUES (?,?,?,?)""", (f.nome,f.end,f.tel, f.cnpj))
        self.conn.commit()


    def get_fornecedores(self):
        fornecedores = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT Nome FROM fornecedores ORDER BY nome DESC """)
        for linha in cursor.fetchall():

            fornecedores.append(linha)

    def delete_fornecedores(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM fornecedores WHERE id = ? """, lista)
        self.conn.commit()
