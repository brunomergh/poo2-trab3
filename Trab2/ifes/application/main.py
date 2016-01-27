import sqlite3
from ifes.cgd.daocliente import DAOCliente
from ifes.cgd.daocompra import DAOCompra
from ifes.cgd.daofornecedor import DAOFornecedor
from ifes.cgd.daoproduto import DAOProduto
from ifes.cgd.daovenda import DAOVenda
from ifes.cgd.daologin import DAOLogin
from ifes.cih.Tela import Tela
from datetime import datetime
import locale

def main():

    conn = sqlite3.connect("padoca.db")

    locale.setlocale(locale.LC_ALL, '')
    hoje = datetime.today()
    dia = hoje.strftime('%A')

    c = DAOCliente()
    c.create_db()

    co = DAOCompra()
    co.create_db()

    f = DAOFornecedor()
    f.create_db()

    p = DAOProduto()
    p.create_db()

    v = DAOVenda()
    v.create_db()

    l = DAOLogin()
    l.create_db()


    Tela().gerencia()



if __name__ == '__main__':
    main()

