__author__ = 'Bruno'

import sqlite3
from ifes.cdp.login import Login

class DAOLogin():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('padoca.db')
        except sqlite3.Error as e:
            print("Error ao conectar com o banco " + e)

    def create_db(self):
        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS logins (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL,
        senha TEXT
        );""")



    def insere_login(self, login):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO logins (login, senha) VALUES (?,?)""", (login.login,login.senha))
        self.conn.commit()


    def get_lista_login(self):
        login = []
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT login FROM logins ORDER BY login DESC """)

        for linha in cursor.fetchall():

            login.append(linha)
        return login

    def get_login(self):
        cursor = self.conn.cursor()
        cursor.execute(""" SELECT login FROM Logins WHERE login = 'admin' """)
        for linha in cursor.fetchall():
            return linha

    def delete_login(self, id):
        lista =[]
        lista.append(id)
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM logins WHERE id = ? """, lista)
        cursor.execute("""DELETE FROM logins WHERE id = ? """, lista)
        self.conn.commit()



