__author__ = 'Bruno'

import sqlite3
from ifes.cdp.pessoa import Pessoa

class DAOCliente():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        fone TEXT,
        end TEXT,
        tipo TEXT,
        Cpf_Cnpj TEXT
        );""")



    def insere_cliente(self, cliente):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO clientes (nome, fone, end, tipo, Cpf_Cnpj) VALUES (?,?,?,?,?)""", (cliente.nome,cliente.tel,cliente.end,cliente.tipo,cliente.cpf_cnpj))
            self.conn.commit()
        except Exception as e:
            raise "Erro ao inserir"



    def get_clientes(self):
        clientes = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT Nome FROM clientes ORDER BY nome DESC """)
        for linha in cursor.fetchall():

            clientes.append(linha)

    def delete_cliente(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM clientes WHERE id = ? """, lista)
        self.conn.commit()



