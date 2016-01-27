__author__ = 'Bruno'

from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaUpDate:

    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,300],[140,300],[216,360]]
        self.ctrl = Control()


    def controle(self):
        self.teclado.capturaTeclas()

        TelaUpdate,TelaInicial = 1, 2
        opcao = TelaUpdate
        papelparede, bsim, seta, bnao = 0,1,2,3
        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[bsim][altura]:
            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and  self.posicao[seta][altura] < self.posicao[bnao][altura]:
            self.posicao[seta][altura] += 60

        sim = (self.posicao[seta][altura] == self.posicao[bsim][altura])
        nao = (self.posicao[seta][altura] == self.posicao[bnao][altura])
        if self.teclado.teclas[self.teclado.enter]:
            if sim:
                self.ctrl.upload()
                opcao = TelaInicial

            elif nao:
                opcao = TelaInicial

        return opcao