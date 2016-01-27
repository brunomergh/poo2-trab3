__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control
from ifes.cgd.daologin import DAOLogin

class ControleTelaLogin:

    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,300],[140,300],[216,360],[216,420]]
        self.ctrl = Control()
        self.listaCadastral = ["", ""]
        self.d = DAOLogin()


    def controle(self):

        TelaLogin,TelaUpdate,TelaInicial = 0,1,2
        self.teclado.capturaTeclas()
        opcao = TelaLogin
        log, sen = 0,1
        papelparede, blogin, seta, bsenha, bconfirma = 0,1,2,3,4
        largura, altura = 0,1





        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[blogin][altura]:
            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and  self.posicao[seta][altura] < self.posicao[bconfirma][altura]:
            self.posicao[seta][altura] += 60

        login = (self.posicao[seta][altura] == self.posicao[blogin][altura])
        senha = (self.posicao[seta][altura] == self.posicao[bsenha][altura])
        confirma = (self.posicao[seta][altura] == self.posicao[bconfirma][altura])

        if self.teclado.teclas[self.teclado.letra] != "":
            if login:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[log])
                    self.pal=self.listaCadastral[log]
                    self.listaCadastral[log]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[log] += self.teclado.teclas[self.teclado.letra]

                return opcao, self.listaCadastral

            if senha:
                if self.teclado.teclas[self.teclado.letra] == "\x08":
                    self.tam=len(self.listaCadastral[sen])
                    self.pal=self.listaCadastral[sen]
                    self.listaCadastral[sen]=self.pal[:self.tam-1]
                else:
                    self.listaCadastral[sen] += self.teclado.teclas[self.teclado.letra]

                return opcao, self.listaCadastral

        if self.teclado.teclas[self.teclado.enter]:

                self.ctrl.cad_login(self.listaCadastral)
                if self.listaCadastral[log] == 'admin' and self.listaCadastral[sen] == 'admin':
                    opcao = TelaUpdate
                else:
                    opcao = TelaInicial

        return opcao, self.listaCadastral
