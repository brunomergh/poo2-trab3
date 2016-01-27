__author__ = 'Bruno'


__author__ = 'Bruno'


from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaRelatorioGerado:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[144,350],[216,350]]
        self.ctrl = Control()


    def controle(self):
        self.teclado.capturaTeclas()

        TelaRelatorioGerado = 12
        TelaRelatorio = 4
        opcao = TelaRelatorioGerado
        papelparede,  seta, bvoltar, = 0,1,2

        largura, altura = 0,1


        brestoque = (self.posicao[seta][altura] == self.posicao[bvoltar][altura])

        if self.teclado.teclas[self.teclado.enter]:
            if bvoltar:
                opcao = TelaRelatorio


        return opcao