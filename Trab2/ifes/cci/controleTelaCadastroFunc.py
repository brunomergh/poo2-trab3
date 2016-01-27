__author__ = 'Bruno'


from ifes.cih.teclado import Teclado
from ifes.cci.control import Control

class ControleTelaCadastroFunc:


    def __init__(self):
        self.teclado = Teclado()
        self.posicao=[[0,0],[216,230],[144,230],[216,290],[216,350]]
        self.ctrl = Control()


    def controle(self):
        self.teclado.capturaTeclas()

        TelaCadCliente = 5
        TelaCadVenda,TelaInicialFunc,TelaCadastroFunc = 9,10,11

        opcao = TelaCadastroFunc
        papelparede,bccliente, seta, bcvenda, bvoltar = 0,1,2,3,4

        largura, altura = 0,1




        if self.teclado.teclas[self.teclado.cima] and self.posicao[seta][altura] > self.posicao[bccliente][altura]:

            self.posicao[seta][altura] -= 60

        if self.teclado.teclas[self.teclado.baixo] and self.posicao[seta][altura] < self.posicao[bvoltar][altura]:

            self.posicao[seta][altura] += 60

        bccliente = (self.posicao[seta][altura] == self.posicao[bccliente][altura])
        bcvenda = (self.posicao[seta][altura] == self.posicao[bcvenda][altura])
        bvoltar = (self.posicao[seta][altura] == self.posicao[bvoltar][altura])

        if self.teclado.teclas[self.teclado.enter]:
            if bccliente:
                opcao = TelaCadCliente
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bcvenda:
                opcao = TelaCadVenda
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230


            elif bvoltar:
                opcao = TelaInicialFunc
                self.posicao[seta][altura] = 144
                self.posicao[seta][altura] = 230

        return opcao