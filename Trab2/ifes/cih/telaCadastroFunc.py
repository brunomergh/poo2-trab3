__author__ = 'Bruno'

from ifes.cih.imprimirNaJanela import ImprimirNaJanela

class TelaCadastroFunc:

    def __init__(self):
        self.imprimi = ImprimirNaJanela()
        self.papelparede, self.bccliente, self.seta, self.bcvenda, self.bvoltar = 0,1,2,3,4





    def imprime(self, janela,posicao):

        self.posicao = posicao
        self.imprimi.imprime(janela,self.posicao[self.papelparede],"PapelParedeCadastrar.jpg",632,632)
        self.imprimi.imprime(janela,self.posicao[self.bccliente],"bccliente.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.bcvenda],"bcvenda.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.bvoltar],"bvoltar2.png",200,50)
        self.imprimi.imprime(janela,self.posicao[self.seta],"seta.png",70,50)